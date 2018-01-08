Python开发
1. 模块开发
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *

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

6.

