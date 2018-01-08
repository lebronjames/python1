# coding:utf-8
import urllib2
import random


def get_html(url, headers, proxies):
    random_userAget = random.choice(headers)
    random_proxy = random.choice(proxies)

    # 下面是模拟浏览器进行访问
    req = urllib2.Request(url)
    req.add_header("User-Agent", random_userAget)
    req.add_header("GET", url)
    req.add_header("Host", "blog.csdn.net")
    req.add_header("Referer", "http://blog.csdn.net/?&page=6")

    # 下面是使用ip代理进行访问
    proxy_support = urllib2.ProxyHandler({"http": random_proxy})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

    html = urllib2.urlopen(req)
    return html


url = "http://blog.csdn.net/?&page=3"
""" 
使用多个主机中的user_agent信息组成一个列表，当然这里面的user_agent都是残缺的，大家使用时可以自己找 
身边的小伙伴借呦 
"""
user_agents = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWe。。。hrome/45.0.2454.101 Safari/537.36",
    "Mozilla / 5.0(Windows NT 6.1) AppleWebKit / 537.。。。。likeGecko) Chrome / 45.0.2454.101Safari/ 537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit。。。。。Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3。。。。ML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) 。。。WebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
    "User-Agent: Mozilla/5.0 (Windows NT 10.0) AppleWebKi。。。。。36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) Apple。。。。。KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
]
# 网上的ip有可能是不能用的，需要多做尝试
myproxies = ["220.189.249.80:80", "124.248.32.43:80"]
html = get_html(url, user_agents, myproxies)
print
html.read()