#!/usr/bin/env python

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from scrapy import Selector
import re
import pandas as pd

def craigslist_scrape(url='https://stlouis.craigslist.org/search/msa'):
    #create pathway and browser
    executable_path = {'executable_path':ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Create a Selector selecting html as the website HTML
    sel = Selector(text=browser.html)
    #pull results from the class containint craigslist listings
    results = sel.xpath('//li[@class="result-row"]')
    
    #list to hold scraped info
    craigslist_data = []

    for i,result in enumerate(results):
        #limit results to first 50
        if i < 51:
            try:
                link = result.xpath('./a/@href').get()
                date = result.xpath('./div/time/@datetime').get()
                listing_no = result.xpath('./div/h3/a/@data-id').get()
                title = result.xpath('./div/h3/a/text()').get()
                price = result.xpath('./div/span[@class="result-meta"]/span[@class="result-price"]/text()').get()
                location = result.xpath('./div/span[@class="result-meta"]/span[@class="result-hood"]/text()').get()
                #convert location to string without parentheses and extra spaces
                regex_location = re.findall(r'\((.*)\s\s', location)
                #append above info to a diction 
                craigslist_dict = {'title':title,
                                   'listing_date':date,
                                   'listing_number':listing_no, 
                                   'price':price,
                                   'location':regex_location[0], 
                                   'listing_url':link}
                #append dictionary to list
                craigslist_data.append(craigslist_dict)
            except Exception as e:
                print(e)

    #return url browser scraped and dataframe of resulting list of dictionaries
    return browser.url, pd.DataFrame(craigslist_data)

    #end and close browser connection
    browser.quit() 