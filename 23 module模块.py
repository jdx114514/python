# 导入模块
import  random
#  import random as r   改名字为 r
for i in range(3):
    print(random.randint(1,100))

#导入模块的功能
from random import randint
#  from random import randint as a  改名字为 a

#导入模块的全部功能
from random import *

for i in range(3):
    print(randint(1,100))