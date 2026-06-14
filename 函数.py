#函数定义
def out_line():
     print('-------------')

#函数调用
out_line()


#计算长方形面积        "长"   "宽"
def rectangle_area(length,width):
       area= length * width
       return area

print(rectangle_area(5,4))

#计算园形面积，周长
def circle_area_len(r):
    return round(3.14*r*r) , round(2*3.14*r) #返回结果   round()四舍五入，去掉小数
print(circle_area_len(5))
area, len = circle_area_len(5)
print(f"面积：{area},长度：{len}")