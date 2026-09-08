num = 100
name = "kim"
def count(r):
    pi = 3.14
    area = pi * r *r
    num = 10000    #函数的变量属于局部变量，只能在函数内使用 ，运行便销毁
    print(num)
    global name    #  global 声明为全局变量，可以在全局使用
    name = "Jack"
    return area

c_area = count(10)
print(c_area)
print(num)  #100
print(name) #Jack

# 传参
def reg_stu(name,age,gender,city):
    print(f" 注册成功，名字：{name}，年龄：{age},性别：{gender},city:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}  #结束后 “返回” 保存在字典，否则就销毁了

# 位置传参
s = reg_stu("小金",18,"男","东莞")
print(s)

# 关键字传参   顺序可以随意
a = reg_stu(name="小金",age=18,gender="男",city="东莞" )
print(a)

a = reg_stu(age=18,name="小金",gender="男",city="东莞" )
print(a)

# 位置传参+关键字传参   必须位置在前
a = reg_stu("小金",18,gender="男",city="东莞")
print(a)



#默认参数
def reg(name,age,gender,city = "东莞"):
    return {"name":name,"age":age,"gender":gender,"city":city}
#没写参数
a = reg(name="小金",age=20,gender="男" )  #没写参数，则填写默认参数
print(a)
#写了参数
a = reg(name="小金",age=20,gender="男",city ="深圳"  )
print(a)                    #写参数，则填写了的参数



#不定长参数
#  *不定长位置参数和 **不定长关键字  将不定长位置参数转为 ”元组“，不定长关键字转为 ”字典“
def calc_date(*args,**kwargs):
    """
    传入一批数据，计算最小值，最大值，平均值
    :param args: 不定长位置参数，需要计算的数据
    :param kwargs: 不定长关键字。
          round: 保留小数个数
          print: 决定是否输出

    :return:
    """
    min_date = min(args)
    max_date = max(args)
    avg_date = sum(args) / len(args)

    if kwargs.get("round") is not None:  #.get()在字典中通过key查询value，若没有key则输出 None
        avg_date = round(avg_date,kwargs.get("round"))    #round( ,1) 指定保留小数个数

    if kwargs.get("print") is not None:
        print(f"最小值为:{min_date},最大值为：{max_date}，平均值为：{avg_date}")
    return min_date, max_date, avg_date
print(calc_date(2.1221, 2.122, 342, 232, 223,round=1,print=True))

#函数做参数
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def calc(x,y,oper):
    return oper(x,y)

print(calc(2,3,add))         # add(2,3)

# 匿名函数 lambda

#加法
add=lambda x,y: x+y
print(add(2,4))

#根据元素的字符个数，从小到大
data_list = ["C++","C","python","Jack","PHP","Java","Go","JaveScript","Rust"]

# 默认从小到大
data_list.sort(key=lambda item:len(item))
print(data_list)

# 颠倒为从大到小
data_list.sort(key=len, reverse=True)  # reverse 相反的
print(data_list)

