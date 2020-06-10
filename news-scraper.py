# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:33:06 2020

@author: noble
"""


import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site = site
        
    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                
news = "https://news.google.com/"
Scraper(news).scrape()