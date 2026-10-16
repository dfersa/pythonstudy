def  countsanjiao(d,g):
    return round(d*g/2)
def num_str(s):
    t="aeiouAEIOU"
    num=0
    for i in s:
        if i in t:
            num+=1
    print("个数为:",num)
def p_gdp(a):
    print("最高分为:",max(a))
    print("最低分为:",min(a))
    t=0
    for i in a:
        t+=i
    print("平均分为:",t/len(a))

d=int(input("请输入三角形的底"))
g=int(input("请输入三角形的高"))
print("三角形面积为:",countsanjiao(d, g))
s=input("请输入要判断的字符串")
num_str(s)
score=(222,132,555,656,745)
p_gdp(score)
