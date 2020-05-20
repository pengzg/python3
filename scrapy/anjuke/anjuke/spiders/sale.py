# -*- coding: utf-8 -*-
import scrapy


class SaleSpider(scrapy.Spider):
    name = 'sale'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
