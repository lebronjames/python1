from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
from urllib.request import urlretrieve
import random
import re

def getHtml(url, headers):
    """
    此函数用于抓取返回403禁止访问的页面
    """
    random_header = random.choice(headers)
    """
    对于Request的第二个参数headers，它是字典型参数，所以在传入时
    也可以直接将个字典传入，字典就是下面元祖的键值对应
    """
    req = Request(url)
    req.add_header("User-Agent", random_header)
    req.add_header("GET", url)
    req.add_header("Host", "tieba.baidu.com")
    req.add_header("Referer", "http://tieba.baidu.com/p/4792769205")

    html = urlopen(req)
    return html

url = "http://tieba.baidu.com/p/4792769205"
#这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的
my_headers = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"]
html = getHtml(url,my_headers)
bsObj = BeautifulSoup(html,"html.parser")
# imageList是存放img标签的列表
imageList = bsObj.findAll("img",{"src":re.compile("http://imgsrc.baidu.com/forum/w%3D580/sign=.+\.jpg")})
for index,image in enumerate(imageList):
    imageUrl = image["src"] #img中网址，也就是图片的网址
    imageLocation = "D://picture/" + str(index+1) + ".jpg" # 图片保存的地址，这里动态命名为数字.jpg
    
