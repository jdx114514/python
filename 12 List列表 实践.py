 #将两个列表合并检查重复
num1_list = [1,2,3,4,5]
num2_list = [1,3,4,6,8]
num_list = num1_list + num2_list
print(num_list)
new_list = []  #建立一个空的列表
for num in num_list:   #挨个把合并列表检查
     if num not in new_list:  #检查在不在新列表，如果不在填入
         new_list.append(num)
print(new_list)



#输入数字整理
num_list = []
for i in range(5):
    num=int(input("请输入"))  #转换成整数
    num_list.append(num)  #依次加入
num_list.sort()  #排序
print(num_list)
print("最小值",min(num_list))   #min()最小值
print("最大值",max(num_list))    #max()最大值
print("平均值",sum(num_list)/len(num_list))   #sum()求和 全部加起来   len()长度  计算全部元素

#生成 1-10的平方列表
num1_list = []
for num in range(1,10):
    num=num**2
    num1_list.append(num)
print(num1_list)

 #选出偶数，并生成一个新的平方列表
nun2_list = [13,312,2,50]
new_list = []
for num in nun2_list :
      if num % 2 == 0 :
          num=num**2
          new_list.append(num)
print(new_list)
