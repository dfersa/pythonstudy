account=123
userpass=888
a=int(input("请输入账号"))
b=int(input("请输入密码"))
if account!=a or userpass!=b:
    print("登录失败")
    exit()
print("登录成功")