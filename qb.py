# coding:utf-8
import requests;
from bs4 import BeautifulSoup



filename = "data.txt"

with open(filename,'a') as f:
	for i in range(1,20): 
		print(i)
		url = "https://www.qiushibaike.com/imgrank/page/"+str(i)

		wbdata = requests.get(url).text
		# 对获取到的文本进行解析
		soup = BeautifulSoup(wbdata,'lxml')
		# 从解析文件中通过select选择器定位指定的元素，返回一个列表
		news_titles = soup.select("div.content span");

		for n in news_titles:
			print(n.get_text())
			f.write(n.get_text()+"\n")