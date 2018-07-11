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
x1 = (-b+math.sqrt(d))/(2*a)
x2 = (-b-math.sqrt(d))/(2*a)

print ("%.1f" %x1)
print ("%.1f" %x2)