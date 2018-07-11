#輸入
import math
a = input ()
b = input ()
c = input ()
a = int (a)
b = int (b)
c = int (c)
#計算
d = b*b-4*a*c

if d >=0:
    x1 = int((-b+math.sqrt(d))/(2*a)*10)/10.0
    x2 = int((-b-math.sqrt(d))/(2*a)*10)/10.0
    print ("%.1f" %x1)
    print ("%.1f" %x2)
elif d < 0:
    x3= int((-b)/(2*a)*10)/10.0
    x4= int((math.sqrt(abs(d)))/(2*a)*10)/10.0
    if x4<0:
        x4=abs(x4)
        print ("%.1f-%.1fi" %(x3 , x4))
        print ("%.1f+%.1fi" %(x3 , x4))
    else:
        print ("%.1f+%.1fi" %(x3 , x4))
        print ("%.1f-%.1fi" %(x3 , x4))
