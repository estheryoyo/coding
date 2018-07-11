a = input ()
#切割字串
a = a.split(' ') 
#list conversion 字串轉數字
a[:] = [int(x) for x in a]
#計算平均數
total = a[0]+a[1]+a[2]+a[3]+a[4]
ave = total / 5
ans = (int (ave*100)/100)
print ("%.2f" %ans)
#變異數
variance = ((a[0]-ans)**2+(a[1]-ans)**2+(a[2]-ans)**2+(a[3]-ans)**2+(a[4]-ans)**2) / 5
print ("%.2f" %variance)
#標準差
cal = variance ** 0.5
sd = (int (cal*100)) / 100
print (sd)