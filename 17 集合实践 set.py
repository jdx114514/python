# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"通天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

#1 找出同时修法语和艺术的同学
print(french_set.intersection(art_set))

#   第二种方法 &交集
print(french_set & art_set)

# 2 找出修了四门课的同学
a = french_set & art_set & basketball_set & football_set
print(a)

#  3 找出选了足球，但没选篮球的同学
print(football_set.difference(basketball_set))

#  方法二
for x in football_set:
    if x not  in basketball_set:
      print(x,end=",")

# 统计每个同学的选修课程
all_set = football_set | basketball_set | art_set | french_set  #统计总名单,一个人只统计一次，set的去重
all_list = [*football_set, *basketball_set, *art_set, *french_set] #统计总次数
for s in all_set:
    print(f"{s} 次数: {all_list.count(s)}")  #f" "格式化  自动把变量添加花括号{}