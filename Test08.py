""""
1. lambda:lambda是Python中一个很有用的语法，它允许你快速定义单行最小函数。类似于C语言中的宏，可以用在任何需要函数的地方
2. filter:filter函数相当于一个过滤器，函数原型为：filter(function,sequence),
表示对sequence序列中的每一个元素依次执行function，这里function是一个bool函数
3. map:map的基本形式为：map(function,sequence)，是将function这个函数作用于sequence序列，然后返回一个最终结果序列
4. reduce:reduce函数的形式为：reduce(function,sequence,initVal)，
function表示一个二元函数，sequence表示要处理的序列，而initVal表示处理的初始值。
5. apply:apply是用来间接地代替某个函数
"""

add = lambda x,y : x + y
print(add(1,2))

sequence = [1,2,3,4,5,6,7,8,9,10]
fun = lambda x : x % 2 == 0
seq = filter(fun,sequence)  #筛选出sequence中的所有偶数
print(seq)


def filter(fun, seq):
    filter_seq = []
    for item in seq:
        if fun(item):
            filter_seq.append(item)
    return filter_seq


seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
fun = lambda x, y: x + y

print(reduce(fun, seq, 0))


def reduce(fun, seq, initVal=None):
    Lseq = list(seq)
    if initVal is None:
        res = Lseq.pop(0)
    else:
        res = initVal
    for item in Lseq:
        res = fun(seq, item)
    return res

def say(a, b):
    print(a, b)


apply(say, (234, 'Hello World!'))