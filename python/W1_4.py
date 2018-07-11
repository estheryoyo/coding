a = input ()
#切割字串
a = a.split(' ')
#list conversion 字串轉數字
a[:] = [int(x) for x in a]
t = (a[0])
y = (a[1])
u = (a[2])
 
#三角形條件式
if (t+y<=u) or (t+u<=y) or (u+y<=t) or t<=0 or u<=0 or y<=0:
    print (1)
elif t==y==u:
    print (2)
elif (t**2+y**2==u**2) or (t**2+u**2==y**2) or (y**2+u**2==t**2) or t==y or t==u or y==u:
    print (3)
else:
    print (4)