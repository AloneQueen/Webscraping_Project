#!/usr/bin/env python

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from scrapy import Selector
import re
import pandas as pd

def craigslist_scrape(url='https://apod.nasa.gov/apod/archivepix.html'):
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
                link = result.xpath('./b/a/@href').get()
                date = result.xpath('./b/@data-id').get()
                description = result.xpath('./b/a/@data-id').get()
                craigslist_dict = {'description':description,
                                   'date':date,
                                   'url':link}
                #append dictionary to list
                craigslist_data.append(craigslist_dict)
            except Exception as e:
                print(e)

    #return url browser scraped and dataframe of resulting list of dictionaries
    return browser.url, pd.DataFrame(craigslist_data)

    #end and close browser connection
    browser.quit() 
