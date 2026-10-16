score=(("s001","王林",85,92,78),
       ("s002","李慕婉",92,88,95),
       ("s003","十三",78,85,82),
       ("s004","十四",88,79,91),
       ("s005","曾牛",95,96,89),
       ("s006","王卓",73,82,77)
       )
yw,sx,yy=[],[],[]
yxxs=[]
for a in score:
    pjf=round((a[2]+a[3]+a[4])/3)
    print(a[1],"总分:",a[2]+a[3]+a[4],"平均分",pjf)
    if pjf>90:
        yxxs.append(a[1])
    yw.append(a[2])
    sx.append(a[3])
    yy.append(a[4])
print("语文",min(yw),max(yw),round(sum(yw)/len(yw)))
print("数学",min(sx),max(sx),round(sum(sx)/len(sx)))
print("英语",min(yy),max(yy),round(sum(yy)/len(yy)))
