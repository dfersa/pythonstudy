print("w/W/上：角色向上移动")
print("s：角色向下移动")
print("a：角色向左移动")
print("d：角色向右移动")
print("\" \"k:跳跃")
print("j:攻击")
print("esc:退出")
while True:
    c=input("请输入操作:")
    match c:
        case "w"|"W"|"上":
            print("角色向上移动了。。")
        case "s":
            print("角色向下移动了。。")
        case "a":
            print("角色向左移动了。。")
        case "d":
            print("角色向右移动了。。")
        case " "|"k":
            print("角色跳跃了。。")
        case "j":
            print("角色攻击了。。")
        case "esc":
            print("bye")
            break
        case _:
            print("输入非法！")
