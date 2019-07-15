# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from tencent.items import NewsItem
from bs4 import BeautifulSoup

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['qq.com']
    start_urls = ['https://www.qq.com']
    # allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        #======
        soup = BeautifulSoup(response.text)
        titles = soup.select('.yw-list li')
        for title in titles:
            print('title->'+title.find('a').get_text()+'\n')
            print('link->'+title.find('a').attrs['href']+'\n')
        #======
        

        #======
        # newsList = response.css('.yw-list li')
        # print(newsList)
        # for news in newsList:
        #     print(news.css('a::text').extract_first())
        #======

        
        