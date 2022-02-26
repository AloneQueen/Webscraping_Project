#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def craigslist_scrape(url='https://stlouis.craigslist.org/search/msa'):
    executable_path = {'executable_path':ChromeDriverManager().install()}

    browser = Browser('chrome', **executable_path, headless=False)

    #direct browser to home page
    browser.visit(url)

    html = bs(browser.html, 'html.parser')

    # Create a Selector selecting html as the website HTML
    #sel = Selector(text=html)

    return html