# coding:utf-8
import requests;
from bs4 import BeautifulSoup



filename = "data.txt"

with open(filename,'a') as f:
	for i in range(1,2): 
		print(i)
		url = "https://www.697www.com/Html/62/index-"+str(i)+".html"
		#url = "https://www.qiushibaike.com/imgrank/page/"+str(i)

		wbdata = requests.get(url)
		print(wbdata.apparent_encoding)
		wbdata.encoding = 'UTF-8-SIG'
		print(wbdata.text)
		# 对获取到的文本进行解析
		# soup = BeautifulSoup(wbdata,'lxml')
		# print(soup)
		# 从解析文件中通过select选择器定位指定的元素，返回一个列表
		# news_titles = soup.select("div.movie_list ul li a h3")

		# for n in news_titles:
		# 	print(n.get_text())
		# 	f.write(n.get_text()+"\n")