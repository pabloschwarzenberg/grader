from math import *

li = []
i = eval(input())
r = i % 2
d = trunc(i / 2)

li.append(r)

while d > 1:
    r = d % 2
    d = trunc(d / 2)
    li.append(r)

li.append(d)

li.reverse()

res = ""
for it in li:
    res += str(it)

print("resultado=" + str(res))
