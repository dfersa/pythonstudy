def check(yh=0,jf=0,yf=988.0,**args):
    total=0.0
    for k in args: #*arg调用 不加*
        total+=k["price"]*k["num"]
    print(total)
    return total-yh-jf//100+yf


checks =check({"iphone":{"price":9999,"num":8}},
            {"dji":{"price":6999,"num":2}},
            {"pro6000":{"price":1,"num":8}}
      )
print(checks)