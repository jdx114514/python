m = int(input("宽度"))
n = int(input("长度"))
for  e in range(n):
    for i in range(m):
        print("*", end = "")  #end()表示每次以什么结尾
    print()
#先循环第一遍"n"循环,再循环"m"全部，后循环第二遍"n"循环


for i in range(1,10): #i=行号
    for j in range(1,i+1): #j=列号，每次循环不超过 i
        print(f" {i} X {j} = {j*i} ", end ="\t") #f"..." 是格式化字符串，把大括号 {} 里的变量直接算出结果并显示出来
        # end="\t" 表示打印完不换行，而是制表符（相当于按一下 Tab 键），让每一列对齐
    print() #当某一行的公式全部打印完后，执行一次换行，准备打印下一行
