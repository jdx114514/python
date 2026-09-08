total = 0
i = 1
while i <= 100:
     if i % 2 == 0:
            total += i
     i += 1
else :
  print(total)

msg = "Hello -"
for i in msg:    #将字符传送变量 i 中
    print(i)

#计算 1-100的奇数之和
total = 0
for i in range (1,101,1): #（ ） # 包头不包尾
        if i % 2 == 1:
          total += i
print(total)

#计算 100-500之间的三倍属之和
total = 0
for i in range (100,501,1):
    if i % 3 == 0:
       total += i
print(total)