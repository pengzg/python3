from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
r = etree.tostring(html)
print(r.decode('utf-8'))

html = etree.parse('./test.html', etree.HTMLParser())
r = etree.tostring(html)
print(r.decode('utf-8'))

html = etree.parse('./test.html', etree.HTMLParser())
r = html.xpath('//*')
print(r)

html = etree.parse('./test.html', etree.HTMLParser())
r = html.xpath('//li')
print(r)
print(r[0])

html = etree.parse('./test.html', etree.HTMLParser())
r = html.xpath('//li/a')
print(r)

html = etree.parse('./test.html', etree.HTMLParser())
r = html.xpath('//ul//a')
print(r)
r = html.xpath('//ul/a')
print(r)

r = html.xpath('//a[@href="link4.html"]/../@class')
print(r)


r = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(r)

r = html.xpath('//li[@class="item-0"]')
print(r)


r = html.xpath('//li[@class="item-0"]/text()')
print(r)

r = html.xpath('//li[@class="item-0"]/a/text()')
print(r)

r = html.xpath('//li[@class="item-0"]//text()')
print(r)

r = html.xpath('//li/a/@href')
print(r)


text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
r = html.xpath('//li[contains(@class, "li")]/a/text()')
print(r)

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
r = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(r)
