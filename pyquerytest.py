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


html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

doc = pq(html)
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)


parent = items.parents('.wrap')
print(parent)

li = doc('.list .item-0.active')
print(li.siblings())


li = doc('.list .item-0.active')
print(li.siblings('.active'))

print('==================5555555555555555====================')

li = doc('.item-0.active')
print(li)
print(str(li))

lis = doc('li').items()

print(type(lis))

for li in lis:
    print(li, type(li))

print('=================66666666666666666666===============')

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)


a = doc('a')
for item in a.items():
    print(item.attr('href'))

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''


doc = pq(html)
a = doc('.item-0.acitve a')
print(a)
print(a.text())

span = doc('.item-0.active a span')
print(span)
print(span.text())

doc = pq(html)
li = doc('.item-0.active')
print(li)
print(li.html())

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))

print('==================777777777777777777===================')

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

html = '''
<ul class="list">
     <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>变换的数据</span>')
print(li)

html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
new = wrap.remove('p')
print(new)
print(new.text())


print('======================888888888888888888======================')
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
li = doc('li:first-child')
print(li)

li = doc('li:last-child')
print(li)

li = doc('li:nth-child(2)')
print(li)

li = doc('li:gt(2)')
print(li)

li = doc('li:nth-child(2n)')
print(li)

