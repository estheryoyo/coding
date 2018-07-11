#輸入網內.網外.市話.簡訊1.簡訊2
s1 = int(input())
s2 = int(input())
c3 = int(input())
m4 = int(input())
m5 = int(input())

#計算183方案
a = s1 * 0.08
b = s2 * 0.139
c = c3 * 0.135
d = m4 * 1.128
e = m5 * 1.483
to1 = a + b + c + d + e
#超出額度$
ans = int(to1 - 183)

#383方案
f = s1 * 0.07
g = s2 * 0.130
h = c3 * 0.121
i = m4 * 1.128
j = m5 * 1.483
to2 = f + g + h + i + j
#超出額度$
ans1 = int(to2 - 383)

#983方案
k = s1 * 0.06
l = s2 * 0.108
m = c3 * 0.101
n = m4 * 1.128
o = m5 * 1.483
to3 = k + l + m + n + o
#超出額度$
ans2 = int(to3 - 983)

#最佳方案 & $$
if to1 < 183:
    print(183)
    print(183)
elif to1 > 183 and to1 < 383:
    print(183)
    print(to1 + ans)

elif to2 < 383:
    print(383)
    print(383)
elif to2 > 383 and to2 < 983:
    print(383)
    print(383 + ans1)

elif to3 < 983:
    print(983)
    print(983 + ans2)
