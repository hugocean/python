import requests
import re

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
code = requests.get('http://jandan.net/2018/03/12/victorian-diet.html',headers = header)
html = code.text

pattern = re.compile('<p>.*</p>')
groups = pattern.findall(html)

for text in groups:
    text = text.replace('<p>','')
    text = text.replace('</p>', '')
    print(text)