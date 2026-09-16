try:
       print(my_name)
      # print(1 / 0)

except NameError as e:
      print("程序运行出错,异常信息:",e)
except ZeroDivisionError as e:
      print("程序运行出错,异常信息:",e)
except Exception as e:  #捕获全部异常信息
      print("程序运行出错,异常信息:", e)
finally:  #无论程序是否运行，finally都会
    print("资源释放")

