def check(*args,yh=0,jf=0,yf=988.0):
    total=0.0
    for k in args: #*arg调用 不加*
        for j in k.values():
            total+=j["price"]*j["num"]
    return total-yh-jf//100+yf


checks =check({"iphone":{"price":9999,"num":8}},
            {"dji":{"price":6999,"num":2}},
            {"pro6000":{"price":1,"num":8}},
            yh=1,
            jf=500
      )
print("总金额为:",checks)
#demo错误点
# 1 *a 封装为 元组
# 2 dict 方法名为 .keys() .values .items
# 3 位置参数必须在 *a 前,关键字参数才可以在 任意位置