# coding:utf-8
import requests
from bs4 import BeautifulSoup

# baseUrl = 'https://www.298ca.com'
baseUrl = 'https://hhxx66.com/'

filename = "data.txt"

with open(filename,'a') as f:
	for i in range(10,140): 
		print(i)
		#url = baseUrl+"/Html/60/index-"+str(i)+".html"
		url = baseUrl+"/htm/Video1/"+str(i)+".htm"
		#url = "https://www.qiushibaike.com/imgrank/page/"+str(i)

		wbdata = requests.get(url)
		# print(wbdata.apparent_encoding)
		wbdata.encoding = 'UTF-8-SIG'
		webData = wbdata.text
		# 对获取到的文本进行解析
		soup = BeautifulSoup(webData,'lxml')
		# print(soup)

		# 从解析文件中通过select选择器定位指定的元素，返回一个列表
		# news_titles = soup.select(".content span")
		# for n in news_titles:
		# 	print(n.get_text())
		# 	f.write(n.get_text()+"\n")

		# items = soup.select("div.movie_list ul li")
		# for n in items:
		# 	f.write(n.find('h3').get_text()+'\n')
		# 	print(n.find('h3').get_text()+'\n')
		# 	f.write(baseUrl+n.a.attrs['href']+'\n')
		items = soup.select("div.item ul li h5.text-overflow-2")
		for n in items:
			f.write(n.find('a').get_text()+'\n')
			print(n.find('a').get_text()+'\n')
			f.write(baseUrl+n.a.attrs['href']+'\n')