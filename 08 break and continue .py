while True:
    username = input("请输入正确的名字: ")
    password = input("请输入正确的密码：")
    if username == "" or password == "":
        print("请不为空")
        continue  #中断本次循环，执行下次循环
    if username == "admin" and password == "123":
        print("登录成功")
        break   #break 跳出全部循环
    if username == "gemini" and password == "123":
        print("登录成功")
        break   #break 跳出全部循环
    else :
        print("密码错误")


import random
num_random= random.randint(1,10)  #生成随机数

while True:
    num = int(input("输入一个数: "))
    if num_random > num:
        print("小了")
        continue
    elif num_random < num:
        print("大了")
        continue
    elif num_random == num:
        print("对")
        break
print("答案 ：",num_random)