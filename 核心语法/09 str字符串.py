s = "Hello World"
print(s[0])
print(s[-1])
#  s[4] =("x")  #不可改
#  print(s)

  #切片
print(s[0:6]) #空格也算一个字符

print(s[1:100:-1]) #倒过来

print(s[-1:-6:1])

#不可变性，怎么都改不了本体
a = "Hello - World"

# find() 查找字符串第一次出现的索引位置
a1 =a.find("o")
print(a1)  #2

# count() 统计总共出现次数
a2 =(a.count("o"))
print(a2)  #4

# upper() 转为大写
print(a.upper())  #HELLO - WORLD

# lower() 转为小写
print(a.lower())  #hello - world

# split() #将字符串按照字符切割，并换成列表
alist = a.split("-")
print(alist)   #['Hello ', ' World']

# strip() 去除字符串两端的空格
print(a.strip())  #Hello - World

# replace() 将字符串中的指定字符串替换成新内容
print(a.replace("H","99"))  #99ello - World

# startswith() 判断是否以指定字符串开头，返回布尔值
print(a.startswith("H"))  #True


# endswith()   判断是否以指定字符串结束，返回布尔值
print(a.endswith("d"))   #True


