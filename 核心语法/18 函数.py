#函数定义
def out_line():
     print('-------------')

#函数调用
out_line()


#计算长方形面积
def rectangle_area(length,width):
       """
       根据长方形的长度和宽，计算面积
       :param length: 长度
       :param width: 宽度
       :return: 长方形面积
       """
       area= length * width
       return area

print(rectangle_area(5,4))

#计算园形面积，周长
def circle_area_len(r):
    """
    根据圆形的半径，计算面积和周长
    :param r: 半径
    :return: 面积，周长
    """
    return round(3.14*r*r) , round(2*3.14*r) #返回结果   round()四舍五入，去掉小数
print(circle_area_len(5))

#元组解包
area, len = circle_area_len(5)
print(f"面积：{area},长度：{len}")

