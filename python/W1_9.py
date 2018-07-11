a = input()

#切割字串
a = a.split(' ')

#list conversion 字串轉數字，三角形三邊長
a[:] = [int(x) for x in a]
t = (a[0])
y = (a[1])
u = (a[2])

#---------------------------------------------------不是三角形

if (t + y <= u) or (t + u <= y) or (u + y <= t) or t <= 0 or u <= 0 or y <= 0:
    print('Not Triangle')

#---------------------------------------------------直角三角形

elif (t**2 + y**2 == u**2) or (t**2 + u**2 == y**2) or (y**2 + u**2 == t**2):
    print('Right Triangle')

#---------------------------------------------------鈍角
elif (t**2 + y**2 < u**2) or (t**2 + u**2 < y**2) or (y**2 + u**2 < t**2):
    print('Obtuse Triangle')

#---------------------------------------------------銳角
elif (t**2 + y**2 > u**2) or (t**2 + u**2 > y**2) or (y**2 + u**2 > t**2):
    print('Acute Triangle')
