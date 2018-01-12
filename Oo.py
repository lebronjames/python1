""""
面向对象编程

"""
class MyClass:
    def tell(self):
        print('This is MyClass')
    def __init__(self): #__init__类似于构造函数
        print('MyClass init')
    def __del__(self):
        print('MyClass del')    #__del__类似于析构函数,一旦对象没有引用，就会被析构。

Test = MyClass()
Test.tell()
