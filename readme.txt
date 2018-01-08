Python开发
1. 模块开发
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *

在使用pycharm开发的过程中，要引入第三方模块，
进入pycharm的主界面，单击file-〉settings-〉Project：untitled-〉Project Interpreter，下载第三方源码installed success

2. 标准数据类型
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）

3. __name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

4. python中列表的内置函数sort（）可以对列表中的元素进行排序，而全局性的sorted（）函数则对所有可迭代的序列都是适用的；
并且sort（）函数是内置函数，会改变当前对象，而sorted（）函数只会返回一个排序后的当前对象的副本，而不会改变当前对象。

5. 使用urllib2，使用ip代理抓取网页
使用多个ip地址进行随机地轮流访问，这样被网站检测的概率就很小了，这时候如果我们再使用多个不同的headers，
这时候就有多个ip+主机的组合，访问时被发现的概率又进一步减小了。

6. urlopen抓取网页的html

7. 网络爬虫--BeautifulSoup使用
认识一下BeautifulSoup中我认为最有用处和用到最多的两个函数：find()和findAll()
函数原型：
findAll(tag,attributes,recursive,text,limit,keywords);
find(tag,attributes,recursive,text,keywords);
参数：
tag：标签参数tag前面我们已经看到过很多次了，你可以传一个标签的名称或者多个标签名称组成的python列表作为标签参数。
         例如此代码是返回HTML文档中所有标题标签的列表：.findAll({"h1","h2","h3","h4","h5","h6"})
attributes：属性参数attributes是用一个python字典封装一个标签的若干个属性和对应的属性值。
        例如此代码会返回HTML文档里红色和绿色两种颜色的span标签：.findAll("span",{"class":{"green","red"}})
recursive：递归参数recursive是一个布尔变量。你想抓取HTML文档标签结构里多少层的信息？如果recursive设为True，findAll函数就会根据你的要求去查找标签参数中的所有子标签，以及子标签的子标签。如果recursive设置为False，findAll函数就只查找文档的一级标签。findAll函数默认是支持递归查找的（recursive默认值是True），一般情况下这个参数不需要设置，除非你真正想要了解自己需要哪些信息，而且抓取速度非常重要，那时你可以设置递归参数。
text：文本参数text有点不同，它是用标签的文本内容去匹配，而不是用标签的属性。假如我们想查找前面网页中包含“the prince”内容的标
签数量，我们可以用这个代码：
nameList=bsObj.findAll(text="the prince")
 print (len(nameList))
limit：范围限制参数limit，显然只用于findAll方法。find其实等价于findAll的limit等于时的情形。如果你只对网页中获取的前n项结果感兴趣，就可以设置它。但是需要注意，这个参数设置之后，获得的前几项结果按照网页上的 顺序排序的，未必是你想要的那前几项。
keyword：这个参数可以让你选择那些具有特定属性的标签。

