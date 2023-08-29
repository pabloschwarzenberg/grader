rut=str(input())
a1 = rut[-1]
b1 = int(a1)
a2 = rut[-2]
b2 = int(a2)
a3 = rut[-3]
b3 = int(a3)
a4 = rut[-4]
b4 = int(a4)
a5 = rut[-5]
b5 = int(a5)
a6 = rut[-6]
b6 = int(a6)
a7 = rut[-7]
b7 = int(a7)
rut2 = int(rut)
if(len(rut) > 7):
    a8 = rut[-8]
    b8 = int(a8)
b1 = b1 * 2
b2 = b2 * 3
b3 = b3 * 4
b4 = b4 * 5
b5 = b5 * 6
b6 = b6 * 7
b7 = b7 * 2
if(len(rut) > 7):
    b8 = b8 * 3
if(len(rut) == 7):
    rt = b1 + b2 + b3 + b4 + b5 + b6 + b7
else:
    rt = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8
print(rt)
parte = rt // 11
print(parte)
ppp = rt - (11 * parte)
print(ppp)
dv = 11 - ppp
if(dv == 11):
    dv = 0
if(dv == 10):
    dv = 'K'
print('dv=',dv)