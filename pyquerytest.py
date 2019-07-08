#sudo pip3 install pyquery
from pyquery import PyQuery as pq
import requests

print('===============11111111111111111===================')

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc = pq(html)
print(doc('li'))


print('==================2222222222222222=====================')
doc = pq(url = 'http://cuiqingcai.com')
print(doc('title'))

doc = pq(requests.get('http://www.cuiqingcai.com').text)
print(doc('title'))


doc = pq(filename='test.html')
print(doc('li'))

print('===================33333333333333===================')


html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

print('==================4444444444444444========================')

doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

lis = items.children()
print(type(lis))
print(lis)


lis = items.children('.active')
print(lis)
