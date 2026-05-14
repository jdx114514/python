#如果为Ture，执行if，为False执行else
a= []
if a:
     print("True")
else:
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
