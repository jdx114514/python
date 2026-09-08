#自动去重，无序的
s1 = {"1","2","3","2","3"}
print(s1)  # 只有{1,2,3}    因为无序，因此每次运行位置都不一样
print(type(s1))

#定义空集合
s2 = set()
print(s2)
print(type(s2))

# add() 添加元素
s1.add("55")  #因为无序，因此每次运行位置都不一样
print(s1)   #{'2', '55', '3', '1'}

# remove() 移除指定元素
s1.remove("55")
print(s1)

# pop() 随机删除集合的元素并返回
s1 .pop()
print(s1)

# clear() 清空集合
s1.clear()
print(s1)  #set()

s2 = {"A","B","C"}
s3 = {"C","D","E"}
print(s2)
print(type(s2))

# difference() 求两个集合的差集 (排除第二个的集合的重复元素)
print(s2.difference(s3))  #{'B', 'A'}
print(s3.difference(s2))  #{'D', 'E'}

#union  并集
print(s2.union(s3))   #{'B', 'D', 'E', 'C', 'A'}
print(s3.union(s2))  #{'A', 'B', 'D', 'C', 'E'}



#intersection 交集
print(s2.intersection(s3))  #{'C'}
print(s3.intersection(s2))  #{'C'}