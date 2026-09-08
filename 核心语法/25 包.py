# 调用模块
import utils.my_var

utils.my_var.log_separator4()
utils.my_var.log_separator()

from utils import my_fun
print(utils.my_fun.NAME)


#   使用 from -- import * 导入包下的所有模块，需要在 __init__中__all__ = []
from utils import *
my_var.log_separator2()
print(my_fun.PI)

# 调用模块的功能
from utils.my_var import log_separator3, log_separator4
log_separator3()
log_separator4()