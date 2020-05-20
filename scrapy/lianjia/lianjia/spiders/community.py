# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from lianjia.items import LianjiaItem
from bs4 import BeautifulSoup

class CommunitySpider(scrapy.Spider):
    
    name = 'community'
    allowed_domains = ['lianjia.com']

    start_urls = ['https://jn.lianjia.com/xiaoqu/pg2/']

    def parse(self, response):
        print(type(response))
        print(response)
        print("1111")
        doc = pq(response.text)
       

        newsList = doc('.xiaoquListItem .title a').items()
        print(type(newsList))
        for news in newsList:
            print(news.text()+'\n')
            print(news.attr['href']+'\n')    