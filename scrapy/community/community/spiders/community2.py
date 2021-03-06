# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from community.items import CommunityItem
from bs4 import BeautifulSoup

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['jinan.anjuke.com']
    start_urls = ['https://jinan.anjuke.com/community/p1']

    def parse(self, response):
        print(type(response))
        doc = pq(response.text)
        
        newsList = doc('.maincontent .li-info h3 a').items()
        print(type(newsList))
        for news in newsList:
            print(news.text()+'\n')
            print(news.attr['href']+'\n')
        
        
