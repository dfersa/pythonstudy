print("1.添加购物车")
print("2.修改购物车")
print("3.删除购物车")
print("4.查询购物车")
print("5.添加购物车")
a=1
gouwuche = {}
while True:
    choice=input("请输入要执行的功能:")
    match choice:
        case "1":
            name,price,num = input("请输入商品名称,价格,数量 以逗号隔开").split(",")
            gouwuche[name] = {"price":price,"num":num}
        case "2":
            name, price, num = input("请输入商品名称,价格,数量 以逗号隔开").split(",")
            gouwuche[name] = {"price":price,"num":num}
        case "3":
            name =input("请输入商品名称")
            del gouwuche[name]
        case "4":
            print(gouwuche)
        case "5":
            break
        case _:
            print("输入数据非法!")
#接收多个参数name,price,num = input("请输入商品名称,价格,数量 以逗号隔开").split(",")