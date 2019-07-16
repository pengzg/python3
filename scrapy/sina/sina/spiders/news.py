# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from sina.items import NewsItem
from bs4 import BeautifulSoup

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    def parse(self, response):
        print(type(response))
        doc = pq(response.text)
        newsList = doc('.list_14 li a').items()
        print(type(newsList))
        for news  in newsList:
            print(news.text()+'\n')
            print(news.attr['href']+'\n')
        
        
