""""
对于map()它的原型是：map(function,sequence)，就是对序列sequence中每个元素都执行函数function操作。
而对于zip()，原型是zip(*list)，list是一个列表，zip(*list)返回的是一个元组
"""
a = ['1','2','3','4']
print(map(list,a))  #把列表a中每个元素转化为列表
print(map(int,a))   #把a中每个元素转化为整数

list = [[1,2,3],[4,5,6],[7,8,9]]
t = zip(*list)
print(t)

x = [1,2,3,4,5]
y = [6,7,8,9,10]
a = zip(x,y)
print(a)
