#如果为Ture，执行if，为False执行else
a= []
if a:
     print("True")
else:                  #elif 否则如果，当前面的判断不成立时，才执行
       print("False")  #结果为 False
a= "aa"
if a:
    print("True")
else:
    print("False")   #结果为 True

#本质：如果达标了就给变量存“合格”，没达标就存“继续加油”
height = 160
status="合格" if height>170 else "太矮了"  #太矮了
print(status)

# if和elif条件相同时，执行if
a = 11
if  a:
    print("True")  #满足执行
elif a:
    print("666")    #满足条件2执行
else:
    print("False")  #都不满足执行

   #match...case 模式匹配
day = input("星期几：")
match day:
    case "1":
        print("周一：上班")
    case "2":
        print("周二：上班")
    case "3":
        print("周三：上班")
    case "4":
        print("周四：上班")
    case "5":
        print("周五：上班")
    case "6"| "7":          # "x" | "y"  相同条件  "|"或的意思
        print("休息天")
    case _:                 # _ : 匹配其他条件   相当 else
        print("输错了")


num1=int(input("数字"))
num2=int(input("数字"))
oper=input("请输入运算符：")
match oper:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("输错了")

