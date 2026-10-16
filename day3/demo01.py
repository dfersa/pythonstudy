# a=[2,3,4,5,5,6]
# a[0]=4 #修改a中的2为4
# #del a[1] #删除a中的3
#
# #切片左闭右开
# c=a[:2] #c值:[4,3]
# print(c)
# print(type(c))
# c=a[1:5:2] #c值:[3,5]
# print(c)
# str = ["咋","不好"]
# print(type(str))
# a=((1,2,3),(2,3),(1,2,3,4))
# print(a)|
a=set() #创建 set里面数据是{1,2}
b={1,2,3}
c={3,4,5,6}
print(type(a))
print(type(b))

aaa= {aa for aa in c if aa not in b}
print(aaa)
ab={"张三":{"age":18,"sex":"male","num":2},"李四":{"age":20,"sex":"female","num":5}}
aaaa= {aa["age"]*aa["num"] for aa in ab.values()}

print("-"*30)
print(ab.get("张三"))
print("-"*30)
bc=[a for a in ab.items()]
print(type(bc))
print(bc)

print(type(aaaa))

#不能 a={} 创建.这创建的是一个dict