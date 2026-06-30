# __all__ 指定 form -- import * 的内容
__all__ = ['log_separator','log_separator2','log_separator3','log_separator4',"PI"]


# 常量 不做修改 （用大写）
PI = 3.1415926

def log_separator():
    print("-" * 30 )

def log_separator2():
    print("+" * 30 )

def log_separator3():
    print("#" * 30 )

def log_separator4():
    print("*" * 30 )


# 测试
# __name__ python中的内置变量，表示当前模块的名字（运行当前模块，__name__为"__main__" , 当模块被导入时，__name__ = 模原的名字
print(__name__)

if __name__ == "__main__":
   log_separator()