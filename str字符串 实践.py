 #判断回文
name = input("请输入：")
name2 = name[-1::-1]   #步长-1向左，空自动补齐
print(name2)
if name2 == name :
    print("正确")
else:
      print("错误")


  #判断邮箱
mail =  input("请输入邮箱：")
if mail.count("@") == 1 and "." in mail :  #count()统计次数   #"" in 判断是否在字符串
    print("正确")
else:
     print("错误")