#通过urllib库的 retrieve将图片保存到文件
#urlretrieve(http,文件名，reporthook，date)
#用xpath获取图片地址

import requests
from lxml import etree
from urllib.request import urlretrieve
http = 'https://movie.douban.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
req = requests.get(http,headers = header)
html = req.text

tree = etree.HTML(html)  #将文档转为一个可以被遍历的树形结构 print输出树的根节点
result = tree.xpath('//*[@id="screening"]/div/ul/li/ul/li/a/img/@src')
#通过浏览器copy xpath //*[@id="screening"]/div[2]/ul/li[20]/ul/li[1]/a/img  需要什么就在后面加@...

download_path = 'E://download url/'

for link in result:
    print('downloading')
    urlretrieve(link,download_path + link[-10] + '.jpg')  #不知道为什么获取的图片没有.什么 所以加了.jpg
