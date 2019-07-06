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
