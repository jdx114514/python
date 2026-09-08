#计算n的阶乘
#递归调用 就是在函数中调用自己  一定要有终结点



def num (x):
    if x == 1:                  # num(3) = 3 * num(2)  开始递
        return 1                # num(2) = 2 * num(1)  还在递
                                # num(1) = 1            终结点
    else:                       # num(2) = 2 * 1 = 6   开始归
        return x * num(x-1)     # num(3) = 3 * 2 = 6   结束归
print(num(1))
print(num(3))
#定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。

#  1.优惠券需要商品总金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
#  2.积分抵扣需要商品总金额满 5000 才可以使用，100的积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
def calc_order_cost(*args:tuple[str,float,int],coupon:int,score:int,express:float):
    """
    根据传入的一批商品信息（商品名，价格，数量），优惠（优惠券，折扣），运费
    :param args: 商品信息（商品名，价格，数量） -----> (苹果，5，2）
    :param coupon: 优惠券
    :param score: 积分折扣
    :param express: 运费
    :return: 订单总价
    """
#订单总价 = 商品总价格 — 优惠券 — 折扣 + 运费
#1.计算总商品价格
    total_price = [goos[1] *goos[2]  for goos in args]  #列表推导式  先将args遍历一次，装进变量goos，再查询相乘
    toa_cost = sum(total_price)
#2.计算优惠券
    if toa_cost >= 5000:
      toa_cost -= coupon
#3.计算积分折扣
    if toa_cost >= 5000 and score//100 < toa_cost:
      toa_cost -= score//100
#4。计算运费
    toa_cost += express
    return toa_cost

print(calc_order_cost(("mimi",1000.9,6),coupon=10,score=100,express=0))

