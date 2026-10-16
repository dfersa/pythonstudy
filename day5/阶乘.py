def dg(a):
    if a==1:
        return 1

    return a*dg(a-1)

i=int(input("请输入你要算的阶乘:"))
print("阶乘结果为:",dg(i))