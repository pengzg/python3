# -*- coding: utf-8 -*-
import scrapy


class CommunitySpider(scrapy.Spider):
    name = 'community'
    allowed_domains = ['anjuke.com']
    start_urls = ['http://anjuke.com/']

    def parse(self, response):
        pass
