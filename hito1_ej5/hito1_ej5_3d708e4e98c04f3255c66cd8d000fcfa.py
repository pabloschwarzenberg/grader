from math import *

i = int(input())
li = [int(x) for x in str(i)]
ref = []

mult = 2

li.reverse()

for item in li:
    if mult > 7:
        mult = 2
    calc = item*mult
    ref.append(item * mult)
    mult += 1

pre = 0
for item in ref:
    pre += item

mod = trunc(pre / 11)
pre = pre - (mod * 11)
res = 11 - pre

if res == 11:
    res = 0
elif res == 10:
    res = "K"

print("dv=" + str(res))
