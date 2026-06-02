#根据成绩单完成查询
students = (
   ("S001", "王林", 85, 92, 78),
   ("S002", "李莫", 92, 88, 95),
   ("S003", "十三", 78, 85, 82),       #大元组包含了楼个下元组
   ("S004", "曾牛", 88, 79, 91),
   ("S005", "周铁", 95, 96, 89),
   ("S006", "王作", 76, 82, 77),
  )
#  1.1计算每个学生成绩，各科平均分，一并输出
for s in students:
  total = (s[2]+s[3]+s[4])//3   #循环查找小元组
  print(s[0],s[1],total)

#  方法二  解包
for a,b,c,d,e in students:
    total = (c+d+e)//3
    print(a,b,total)


#1.2统计各科最高值和最低值,平均值
num1 = [s[2] for s in students ]
num2 = [s[3] for s in students ]
num3 = [s[4] for s in students ]
print("语文最高分",max(num1),"数学最高分",max(num2),"英语最高分",max(num3))
print("语文最低分",min(num1),"数学最低分",min(num2),"英语最低分",min(num3))
print("语文平均分",sum(num1)//len(num1),"数学平均分",sum(num2)//len(num2),"英语平均分",sum(num3)//len(num3))  #len()计算括号多少元素

#1.3  查找平均成绩大于90的同学
for s in students:
    total = (s[2]+s[3]+s[4])//3
    if total>=90:
        print(s[0],s[1],total)

#方法二  解包
for a,b,c,d,e in students:
    total = (c+d+e)//3
    if total>=90:
        print(a,b,total)
