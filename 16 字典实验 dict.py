
shopping_cart = {}

# 1. 制作菜单
print("欢迎使用购物车管理系统 ~")
menu = """
########### 购物车系统 ###########
#           1.添加购物车         #
#           2.修改购物车         #
#           3.删除购物车         #
#           4.查询购物车         #
#           5.退出购物车         #
################################
"""
print(menu)

# 2. 执行的具体操作
while True:
    cho = int(input("请选择功能："))
    match cho:
        case 1:  # 添加购物车
            good_name = input("商品名称")
            good_num = int(input("商品数量"))
            good_price = float(input("商品价格"))
            if good_name in shopping_cart:
                print("商品已用，请重新选择")
            else:
                shopping_cart[good_name] = {"价格": good_price, "数量": good_num}  # shopping_cart[good_name] 嵌套字典
                print("添加完成")  # shopping_cart ={"good_name":{"价格":good_price,"数量":good_num},{}  }
        case 2:  # 修改购物车
            good_name = input("请输入修改商品名称")
            if good_name not in shopping_cart:
                print("购物车中没有，请重新选择")
            else:
                new_num = int(input("最新商品数量"))
                if new_num == shopping_cart[good_name]["数量"]:
                    print("数量相同，无需修改")
                else:
                  shopping_cart[good_name]["数量"] = new_num   #从右给左赋值
                  print("修改成功")
        case 3:  # 删除购物车
            good_name = input("请输入删除商品名称")
            if good_name not in shopping_cart:
                print("购物车中没有，请重新选择")
            else:
                del shopping_cart[good_name]
                print("删除成功")

        case 4:  # 查询购物车
            for good_name in shopping_cart.keys():
                good_info = shopping_cart[good_name]
                print(f'商品名称：{good_name}，商品价格：{good_info["价格"]},商品数量：{good_info["数量"]}')

        case 5:  # 退出购物车
            break
        case _:
            print("非法操作，请重新")