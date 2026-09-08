# 定义类
class Car:
    #__init__ 方法是初始化的方法，会在对象创建时自动调用，可以在方法中为对象设置对应的属性
    #self   是第一个参数，表示当前创建出来的实例对象
    def __init__(self, c_color,c_brand, c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
c1 = Car("红色","BMW","X7",70000)

print(c1.__dict__) #将对象的属性以字典的形式输出

