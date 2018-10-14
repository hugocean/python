#从视频零基础学习爬虫写的
#用的是 suop获取的图片地址

import requests,urllib.request
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/5149504613?pn=1'
url2 = 'http://desk.zol.com.cn/bizhi/7244_89635_2.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
          'Cookie': '_ga=GA1.2.2002481844.1517997105; _gid=GA1.2.1153317059.1520845821'}
source_code = requests.get(url,headers=header)
plain_text = source_code.text

soup = BeautifulSoup(plain_text)

download_links = []  #创建一个列表list 储存图片
download_path = 'E://download soup/'

for pic_tag in soup.find_all('img'):  # 观察图片规则 遍历数据 获取图片链接
    pic_link = pic_tag.get('style')
    download_links.append(pic_link)
    print(download_links)

# for item in download_links:
#     urllib.request.urlretrieve(item,download_path + item[-10:])
#     print('Done')

