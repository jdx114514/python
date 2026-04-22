a=10     #自上往下，从左到右
b=20      #  =等于赋值
c = a    #c=10,a=None
a = b    #a=20,b=None
b = c    #b=20,c=none

print(a,b)

a=100
b=200
c=300
# 让 a b c =  c a b
f = a
a = c
c = b
b = f
print(a,b,c)
a,b,c = a,b,c #或者
print(a,b,c)