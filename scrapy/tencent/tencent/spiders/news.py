# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from tencent.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['qq.com']
    start_urls = ['https://www.qq.com']
    # allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print('====='+response+'================')
        newsList = response.css('.yw-list li')
        print(newsList)
        for news in newsList:
            print(news.css('a::text').extract_first())
        # newsList = doc('.yw-list li')
        # for ite in newsList:
        #     item = NewsItem()
        #     item['title'] = ite.find('a').text()
        #     print(item)
        # scrapy.Request(url=start_urls, callback=self.parse)
        