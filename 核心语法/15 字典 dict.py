# key不可以重复，否则后面的值覆盖前面
dict1 ={"小林":500,"金东":400,"吴填":300,"刘卷":466,"小林":666}
print(dict1)
print(type(dict1))

# key必须是不可变类型（str,int,float,tuple） 不能是 list set dict
dict2 = {1:500,-2:400,1.4:300,(1,3):466,('A','B'):666}
print(dict1)
#访问
print(dict1["金东"])
dict1["金东"] = 500
print(dict1)   #可以修改


dict3 ={"小林":500,"金东":400,"吴起":300,"叶":466}
# key不存在就是添加
dict3["王哥"] = 500
print(dict3)   #{'小林': 500, '金东': 400, '吴起': 300, '叶': 466, '王哥': 500}

# key存在就是修改
dict3["吴起"] = 1
print(dict3)   #{'小林': 500, '金东': 400, '吴起': 1, '叶': 466, '王哥': 500}

#查询
print(dict3["小林"])  #根据key获得value
print(dict3.keys())   #获得所有key
print(dict3.values()) #获得所有value
print(dict3.items())   #获得所有  key:value

# 删除
score = dict3.pop("小林")
print(score)  #500
print(dict3) #{'金东': 400, '吴起': 1, '叶': 466, '王哥': 500}

del dict3  ['叶']
print(dict3)   #{'金东': 400, '吴起': 1, '王哥': 500}

#遍历
for key,value in dict3.items():
    print(key,value)


