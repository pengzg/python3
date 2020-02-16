# -*- coding: utf-8 -*-
import scrapy
import json
from pyquery import PyQuery as pq
from xg.items import XgItem
from bs4 import BeautifulSoup
import pymysql

class XgSpider(scrapy.Spider):
    name = 'xg'
    allowed_domains = ['qq.com']
    start_urls = ['https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province=%E6%B9%96%E5%8C%97']
    # start_urls = ['https://news.qq.com//zt2020/page/feiyan.htm#charts']
    # allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        host = ''
        pwd = ''
        db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='spiders')
        cursor = db.cursor()
     

        #======
        print(response.text)
        data = response.text
        
        #将python字典类型变成json数据格式
        json_str=json.dumps(data)
        print(json_str)
        print(type(json_str))
        #将JSON数据解码为dict（字典）
        data1=json.loads(data)
        print(data1)
        print(type(data1))
        print("dict['ret']: ", data1['ret'])
        print("dict['info']: ", data1['info'])
        print("dict['data']: ", data1['data'])
        print(type(data1['data']))
        for i in range(len(data1['data'])):
            print(type(data1['data'][i]))
            cityItem = data1['data'][i]
            sql = 'INSERT INTO xg(xg_province,xg_country,xg_confirm,xg_confirm_add,xg_heal,xg_dead,xg_date) values(%s, %s, %s, %s, %s, %s, %s)'
            try:
                cursor.execute(sql, (cityItem['province'],cityItem['country'],cityItem['confirm'],cityItem['confirm_add'],cityItem['heal'],cityItem['dead'], cityItem['date']))
                db.commit()
            except:
                db.rollback()



        # soup = BeautifulSoup(response.text)
        # items = soup.select('.chianList')
        # print(items)
        # for item in items:
        #     print('province->'+item.find('.blue').get_text()+'\n')
        #     print('totalnum->'+item.find('.add').get_text()+'\n')
        #======
        

        #======
        # newsList = response.css('.yw-list li')
        # print(newsList)
        # for news in newsList:
        #     print(news.css('a::text').extract_first())
        #======    