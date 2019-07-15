# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from tencent.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['www.qq.com']
    # start_urls = ['www.qq.com']
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print('====='+response+'================')
        doc = pq(response)
        newsList = doc('.yw-list li')
        for ite in newsList:
            item = NewsItem()
            item['title'] = ite.find('a').text()
            print(item)
        scrapy.Request(url=start_urls, callback=self.parse)