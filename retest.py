import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
r = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(r)
print(r.group())
print(r.span())


