fayu={"张三","李四","王五","赵六"}
yishu={"张三","王五","赵六","刘七"}
zuqiu={"张三","李四","刘七"}
lanqiu={"张三","王五","赵六","刘七"}
print("同时选修法语艺术的有:",fayu&yishu)
print("同时选修四门课程的有:",fayu&yishu&zuqiu&lanqiu)
print("选修足球没选篮球的有:",zuqiu-lanqiu)
# a=[s for s in fayu|yishu|zuqiu|lanqiu] 这样写成并集了
# append直接加到最后一个参数是容器也不拆
# extend如果是容器拆开再加入,一个也可以加
#麻烦
# a=[s for s in fayu]
# a.extend([s for s in yishu])
# a.extend([s for s in zuqiu])
# a.extend([s for s in lanqiu])
# *也能除了dict不能解包其他都能解
a=[*fayu,*yishu,*zuqiu,*lanqiu]

print("每一个学生选修的课程数量:")
print("\t\t\t\t\t\t张三:",a.count("张三"))
print("\t\t\t\t\t\t李四:",a.count("李四"))
print("\t\t\t\t\t\t王五:",a.count("王五"))
print("\t\t\t\t\t\t赵六:",a.count("赵六"))
print("\t\t\t\t\t\t刘七:",a.count("刘七"))