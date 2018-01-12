""""
Python 列表测试
堆栈—后进先出
list.append() 向队列尾部添加
list.pop() 从队列尾部删除
队列—先进先出
list.append() 向队列尾部添加
list.pop(0) 从队列头部删除
"""

arr = [1,1,5,6,9,7,3,2,11,56,45,78,100,55,0,5,9,10]
arr.append(89)  #向列表中添加一个对象obj
print(arr)
print(arr.count(5)) #返回一个对象obj在列表中出现的次数

arr1 = [123,456,789]
arr.extend(arr1)    #把序列obj中的内容添加到列表中
print(arr)

arr.insert(1,999)   #在index位置插入对象obj
print(arr)

arr.pop(0)  #删除并返回指定位置的对象，默认是最后一个对象
print(arr)

arr.remove(999) #从列表中删除对象obj
print(arr)

arr.sort()
print(arr)
