#通过xpath获取文字
#抓取发布者名字
#抓取更多的页面内容
#保存数据至文件

import requests
from lxml import etree

http = 'http://jandan.net/duan'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
date_all = ''  #定义一个空字符串 将print都改成向dateall里输入内容
for i in range(3):   #抓取三个页面
    req = requests.get(http,headers = header)
    html = req.text

    tree = etree.HTML(html)  #将文档转为一个可以被遍历的树形结构 print输出树的根节点
    result = tree.xpath('//li//div[@class="text"]')   #Xpath 两个斜杠查找所有节点 对class进行条件匹配 寻找需要的节点

    for div in result:
        author = div.xpath('../div[@class="author"]/strong/text()') #抓取发布者的名字 ..表示当前位置的上一级
        #print(author[0])
        date_all += (author[0] + ':\n')
        content = div.xpath('p/text()') #从当前位置的子节点选取 文本内容
        for p in content:   #遍历列表
            #print(p)
            date_all += p
        #print('=======')
        date_all += '\n\n'

    current_page = tree.xpath('//span[@class="current-comment-page"]/text()') #观察网页 网站用current-comment-page保存当前页面
    next_page = int(current_page[0].strip('[]'))-1 #对页面号进行处理 得到下个页面号

    http = 'http://jandan.net/duan/page-%d' %next_page  #抓取页面的地址更新
    #print('PAGE:',next_page,http)
    #date_all += ('PAGE:',next_page,http)

with open('jokes.text','w',encoding='utf-8') as f:  #全部抓取完通过with open()打开一个文件，将date_all里的文件保存进去
    f.write(date_all)
