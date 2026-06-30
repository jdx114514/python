#不可修改
t1 = (1,2,3,3,2,1)
print(type(t1))
print(t1[0:])

#如果定义一个元素的元组，要加个逗号
a = (100,)
b = (100)
print(type(a),type(b))  #<class 'tuple'> <class 'int'>

# count()统计个数
print(t1.count(1))  #2

# index() 获得元素的索引(第一个)
print(t1.index(3))  #2

#组包   两种方式都可以
t1 = (1,2,3,4,5,6)
t2 = 1,2,3,4,5,6
print(t1,t2)  #(1, 2, 3, 4, 5, 6) (1, 2, 3, 4, 5, 6)

#解包
a1,a2,a3,a4,a5,a6 = t1
print(a1,a2,a3,a4,a5,a6)  #1 2 3 4 5 6

#  *扩展解包 (装剩下的元素)
b1,b2,*b3,b4= t1
print(b1,b2,b3,b4)  #1 2 [3, 4, 5] 6

a,b,c,*d= t1
print(a,b,c,d)  #1 2 3 [4, 5, 6]


