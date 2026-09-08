#只是提示，非强制执行
a :int = 596
score :float = 98.5
hobby :str = "python"
flag :bool = True
pic2 :None =  None

name :list[str | int] =["A,B,C"]
phone :set[int] = {1333,1,4}  #集合，自动去重
options :dict[str,int] ={"count":12,"total":1}
goods :tuple[str,int,int] = ("苹果",10,4)

name.append(20200)
print(name)
name.append("3r4r")
print(name)


def clc_score(args :list[int]) -> tuple[int,int,float]:
    min_date = min(args)
    max_date = max(args)
    avg_date = sum(args) / len(args)
    return min_date, max_date, avg_date