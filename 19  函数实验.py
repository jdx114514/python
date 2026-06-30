#嵌套调用  先进后出
def function_a():             # 开始  function_a()
    print("a...before")        # 输出  a...before
    function_b()                # 调用  function_b()
    print("a...after")           # 输出  b...before
                                  # 调用  function_c()
def function_b():                  # 输出   c...
    print("b...before")             # 输出   b...after
    function_c()                     # 输出   a...after
    print("b...after")

def function_c():
    print("c...")

function_a()


# 查找元音字母
def count_aeiou(s):
    """
    统计元音字母个数
    :param s:字符串
    :return:统计个数
    """
    num = 0
    vowels  = "aeiouAEIOU"
    for a in s:
     if a in vowels:
        num += 1
    return num
print(count_aeiou("abcce"))

# 在学生成绩中查找 最大值 最小值 平均值
def clc_score(score_list):
    """
    在学生成绩中查找 最大值 最小值 平均值
    :param score_list: 学生成绩
    :return: 输出最大值 最小值 平均值
    """
    return  round(max(score_list)), round(min(score_list)), round((sum(score_list)/len(score_list)))
print(clc_score([2,10,10]))  #这里使用列表，元组不能修改集合，集合自动去除，然后列表就是万能的，如果没有特殊需求就用它