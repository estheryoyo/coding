#輸入座標數字
a1 = int(input ())
a2 = int(input ())
a = [a1,a2]
a.sort()

b1 = int(input ())
b2 = int(input ())
b = [b1,b2]
b.sort()

c1 = int(input ())
c2 = int(input ())
c = [c1,c2]
c.sort()

t = [a,b,c]
t.sort()

#線段長度計算
lon = t[0][1]-t[0][0]
if t[1][0]>t[0][1]:
    lon = lon + (t[1][1]-t[1][0])
elif t[1][1]>t[0][1]:
    lon = lon + (t[1][1]-t[0][1])
if t[2][0]>t[1][1] and t[0][1]<t[2][0]:
    lon = lon+(t[2][1]-t[2][0])
elif t[1][1]<t[2][1] and t[0][1]<t[2][1]:
    if t[0][1]>t[1][1]:
        lon = lon+(t[2][1]-t[0][1])
    else:
        lon = lon+(t[2][1]-t[1][1])
print (lon)


"""
lon=a2-a1
if b1>a2 :
    lon=lon+(b2-b1)
elif b2>a2 :
    lon=lon+(b2-a2)
if c1>b2 and a2<c1 :
    lon=lon+(c2-c1)
elif b2<c2 and a2<c2 :
    #lon=c2-a1#
    if a2>b2 :
        lon=lon+(c2-a2)
    else :lon=lon+(c2-b2)
print(lon)
"""