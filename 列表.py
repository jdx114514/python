s = [1,2,"kk",3,4,5,]
print(type(s))  #列表类型
print(s[2])    #正向索引
print(s[-1])   #方向索引

#修改
s[0] = "A"
print(s)

#删除
del s[0]
print(s)

#切片
a = ["A","B","C","D","E","F"]
  #a[开始索引:末尾索引:步长]
print(a[0:6:1])  #末尾不输出
  #负数切片
print(a[-1:-7:-1])


a = [1,3,2,4]
# append() :在列表尾部追加元素
a.append(5)
print(a)   #[1, 3, 2, 4, 5]

# insert() :在指定索引之前，插入元素
a.insert(0,"91")
print(a)  #['91', 1, 3, 2, 4, 5]

# remove():移除列表中第一个匹配的元素
a.remove("91")
print(a)   #[1, 3, 2, 4, 5]

# pop() :删除列表中指定索引位置的元素并返回(如果未指定，默认删除最后一个)
e =a.pop()
print(e)  #5
print(a)  #[1, 3, 2, 4]

# sort() :排序
a.sort()
print(a) #[1, 2, 3, 4]

# reverse() :反转列表函数
a.reverse()
print(a)  #[4, 3, 2, 1]