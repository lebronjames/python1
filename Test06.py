"""
Python 字典测试

"""
dict = {'name':'goujinping','age':'21','sex':'man','school':'NEFU'}
print(dict)

print(dict['age'])  #通过键访问相应的值
print(dict['name'])
for key in dict.keys(): #访问字典的键 dict2.keys()，返回一个列表
    print(key)
for value in dict.values(): #访问字典的值 dict2.values(), 返回一个列表
    print(value)

del dict['sex'] #删除字典元素和字典
print(dict)

del dict
print(dict)