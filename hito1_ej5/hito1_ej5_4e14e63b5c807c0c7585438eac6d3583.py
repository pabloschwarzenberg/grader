rut = input("ingrese su rut sin dv: ")
largo = len (rut)
dv = ''
a=int(rut[largo-1])
b=int(rut[largo-2])
c=int(rut[largo-3])
d=int(rut[largo-4])
e=int(rut[largo-5])
f=int(rut[largo-6])
g=int(rut[largo-7])
h=int(rut[largo-8])
if largo ==7:
    h=0
am = (a*2)
bm = (b*3)
cm = (c*4)
dm = (d*5)
em = (e*6)
fm = (f*7)
gm = (g*2)
hm = (h*3)
suma = (am+bm+cm+dm+em+fm+gm+hm)
divsum= suma//11
resto=suma%11
factor = 11-resto
if factor ==11:
    dv=0
elif factor ==10:
    dv='k'
else:
    dv=factor
print ("dv=",dv)


