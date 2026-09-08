class Car:
    # 类属性（所有实例对象共享）
    wheel = 4
    tax_rate = 0.1
    def __init__(self, c_color,c_brand, c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 3

    def running(self):
        print(f"{self.brand} {self.name},正在高速行驶")

    def total_cost(self,discount,rate=0.1):
         """
         计算车的总费用
         :param discount:折扣
         :param rate: 费率
         :return: 总费用
         """
         total_cost = self.price * rate + self.price * discount
         return total_cost
    #魔法方法
    #字符串表示的方法
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price},{self.wheel},{self.tax_rate}"

    #比较两个对象是否相等
    def __eq__(self,other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price

     # __lt__ 小于  __le__ 小于等于 __gt__ 大于 __ge__ 大于等于
    def __lt__(self,other):
        return self.price < other.price
c1 = Car("红色","BMW","X7",700)
print(c1)
print(c1.wheel)  #查找属性时，优先查找实例属性，实例属性不存在，再查找类属性

c2 = Car("红色","BMW","X7",70000)
print(Car.tax_rate)

c3 = Car("白色","奔驰","c300",1000)


print(c1 == c2)
print(c1 < c2)
