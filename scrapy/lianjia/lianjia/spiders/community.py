# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery as pq
from lianjia.items import LianjiaItem
from bs4 import BeautifulSoup
import pymysql

class CommunitySpider(scrapy.Spider):
    
    name = 'community'
    allowed_domains = ['lianjia.com']

    start_urls = ['https://jn.lianjia.com/xiaoqu/pg80/']

    

    def parse(self, response):

        host = '182.92.180.219'
        pwd = 'SCrLzWZUj1Iz7ZUbAzYU'
        db = pymysql.connect(host=host, user='root', password=pwd, port=3306, db='sqhz_dev')
        cursor = db.cursor()
        print(type(response))
        print(response)
        print("1111")
        doc = pq(response.text)
       

        # newsList = doc('.xiaoquListItem .title a').items()
        # print(type(newsList))
        # for news in newsList:
        #     print(news.text()+'\n')
        #     print(news.attr['href']+'\n')    
        newsList = doc('.xiaoquListItem').items()
        print(type(newsList))
        for news in newsList:
            print(news(".title a").text()+'\n')
            print(news(".positionInfo .district").text()+'\n')
            print(news(".positionInfo .bizcircle").text()+'\n')
            print(news(".totalPrice span").text()+'\n')
            sql = 'INSERT INTO jd_bcm(bc_name,bc_dis,bc_price,bc_biz,bc_url) values(%s, %s, %s, %s, %s)'
            try:
                cursor.execute(sql, (news(".title a").text(),news(".positionInfo .district").text(),news(".totalPrice span").text(),news(".positionInfo .bizcircle").text(),news(".title a").attr['href']))
                db.commit()
            except:
                db.rollback() 
            # print(news[0].attr['href']+'\n') 