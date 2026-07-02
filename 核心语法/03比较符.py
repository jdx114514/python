print( 100 == 100 )  #True
print( 100 != 100 )  #False
print( 50 >= 100 )   #False
print( 100 <= 100 )  #True


num = int(input("请输入一个数字："))
print( 10 <= num and num <= 20 )  #寻找 10 到 20 之间的数字
# and 连接条件是并且的关系，两个条件同时为 True 才为True，否则为 False

print( 10 > num or num > 20 )    #判断不是 10 到 20 之间的数字
# or 连接条件是或者的关系 ，只要有一个条件陈立就为 True， 全部不成立才为 False
