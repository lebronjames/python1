# coding:utf - 8
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import random
import re


def getContent(url, headers):
    """
    此函数用于抓取返回403禁止访问的网页
    """
    random_header = random.choice(headers)

    """ 
    对于Request中的第二个参数headers，它是字典型参数，所以在传入时 
    也可以直接将个字典传入，字典中就是下面元组的键值对应 
    """
    # req =Request(url)
    # req.add_header("User-Agent", random_header)
    # req.add_header("GET",url)
    # req.add_header("Host","blog.csdn.net")
    # req.add_header("Referer","http://www.csdn.net/")

    header = {"User-Agent": random_header, "GET": url, "Host": "blog.csdn.net", "Referer": "http://www.csdn.net/"}
    req = Request(url, None, header)
    content = urlopen(req).read().decode("utf-8")
    return content


url = "http://blog.csdn.net/beliefer/article/details/51251757"
# 这里面的my_headers中的内容由于是个人主机的信息，所以我就用句号省略了一些，在使用时可以将自己主机的<span style="color: rgb(84, 84, 84); font-family: 'Segoe UI', Tahoma, sans-serif;  white-space: pre-wrap;"><strong>User-Agent放进去</strong></span>
my_headers = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/53。。。(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"]
print(getContent(url, my_headers))