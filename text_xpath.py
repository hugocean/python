#通过xpath获取文字

import requests
from lxml import etree

http = 'http://jandan.net/duan/page-81#comments'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
req = requests.get(http,headers = header)
html = req.text

tree = etree.HTML(html)  #将文档转为一个可以被遍历的树形结构 print输出树的根节点
result = tree.xpath('//li//div[@class="text"]')   #Xpath 两个斜杠查找所有节点 对class进行条件匹配 寻找需要的节点

for div in result:
    author = div.xpath('../div[@class="author"]/strong/text()') #抓取发布者的名字
    print(author)
    content = div.xpath('p/text()') #从当前位置的子节点选取 文本内容
    for p in content:   #遍历列表
        print(p)
    print('=======')