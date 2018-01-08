#coding:utf-8
from urllib.request import urlopen
html=urlopen("http://tieba.baidu.com/")
print(html.read().decode('utf-8')) #解决中文编码