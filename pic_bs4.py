import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
http = 'http://tieba.baidu.com/p/5149504613?pn=1'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
req = requests.get(http,headers = header)
html = req.text

soup = BeautifulSoup(html,'lxml')
result = soup.find_all('img')
print(result)

download_path = 'E://download soup/'
download_links = []

for pic_tag in soup.find_all('img'):  # 观察图片规则 遍历数据 获取图片链接
    pic_link = pic_tag.get('src')

    download_links.append(pic_link)

#Xpath 方法
#tree = etree.HTML(html)  #将文档转为一个可以被遍历的树形结构 print输出树的根节点
#result = tree.xpath('//*[@id="screening"]/div/ul/li/ul/li/a/img/@src')#通过浏览器copy xpath //*[@id="screening"]/div[2]/ul/li[20]/ul/li[1]/a/img  需要什么就在后面加@...

# for link in download_links:
#     print('downloading')
#     try:
#         urlretrieve(link,download_path + link[-10] + '.jpg')  #不知道为什么获取的图片没有.什么 所以加了.jpg
#     except:
#         print('download error')
#     else:
#         print('saved')