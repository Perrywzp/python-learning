# -*- coding: utf-8 -*-
import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)


r2 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r2.url)
print(r2.encoding)
print(r2.content)


r3 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r3.text)
