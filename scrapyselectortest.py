from scrapy import Selector

body = '<html><head><title>Hello World</title></head><body></body></html>'
selector = Selector(text=body)
print(selector)
title = selector.xpath('//title/text()').extract_first()
print(title)
















