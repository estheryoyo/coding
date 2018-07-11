#輸入3本書
b1 = input()
b2 = input()
b3 = input()

x = int (b1)
y = int (b2)
z = int (b3)

#b1條件式
if x<=10:
    s = x * 380
elif x<=20:
    s = x * 380 *0.9
elif x<=30:
    s = x * 380 * 0.85
else:
    s = x * 380 * 0.8

#b2條件式
if y<=10:
    m = y *1200
elif y<=20:
    m = y *1200 * 0.95
elif y<=30:
    m = y *1200 * 0.85
else:
    m = y *1200 * 0.8

#b3條件式
if z<=10:
    n = z * 180
elif z<=20:
    n = z * 180* 0.85
elif z<=30:
    n = z * 180* 0.8
else:
    n = z * 180* 0.7

print("%d"%(s+m+n))