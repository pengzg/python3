import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
r = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(r)
print(r.group())
print(r.span())

content = 'Hello 1234567 World_This is a Regex Demo'
r = re.match('^Hello\s(\d+)\sWorld', content)
print(r)
print(r.group())
print(r.group(1))
print(r.span())


content = 'Hello 123 4567 World_This is a Regex Demo'
r = re.match('^Hello.*Demo$', content)
print(r)
print(r.group())
print(r.span())

content = 'Hello 1234567 World_This is a Regex Demo'
#r = re.match('^He.*(\d+).*Demo$', content)
r = re.match('^He.*?(\d+).*Demo$', content)
print(r)
print(r.group())
print(r.group(1))
print(r.span())

content = 'http://weibo.com/comment/kEraCN'
r1 = re.match('http.*?comment/(.*?)', content)
r2 = re.match('http.*?comment/(.*)', content)
print('r1', r1.group(1))
print('r2', r2.group(1))

content = '''Hello 1234567 World_This
is a Regex Demo
'''
r = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(r.group(1))


content = '(百度)www.baidu.com'
r = re.match('\(百度\)www\.baidu\.com', content)
print(r)

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
r = re.match('Hello.*?(\d+).*?Demo', content)
r = re.search('Hello.*?(\d+).*?Demo', content)
print(r)

r = re.match('.*?Hell.*D.*', content)
print(r)


html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

# 1.找出 齐秦 往事随风
r = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(r)
print(r.group(1), r.group(2))

#2.任贤齐 沧海一声笑
r = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(r)
print(r.group(1), r.group(2))
#3.beyond 光辉岁月
r = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
print(r)
print(r.group(1), r.group(2))

#找出所有歌手 名字
r = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(r)
print(type(r))
for result in r:
    print(result)
    print(result[0], result[1], result[2])



results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0], result[1], result[2])
