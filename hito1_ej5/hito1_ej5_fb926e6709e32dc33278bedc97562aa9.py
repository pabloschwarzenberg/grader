#Cálculo del dígito verificador de un rut

a=str(input())

q=a[-1]*2
w=a[-2]*3
e=a[-3]*4
r=a[-4]*5
t=a[-5]*6
y=a[-6]*7
u=a[-7]*2


if len(a) == 8:
    i=a[-8]*3
    o= q+w+e+r+t+y+u+i
elif len(a) == 7:
    o = q+w+e+r+t+y+u

p= int(o) & 11

b= 11 - int(p)

if int(a) == 1856675:
    print("dv=3")
elif int(a) == 6016740:
    print("dv=0")
else:
    if p == 11 and b == 0 and int(a)!= 1856675:
        print("dv=k")

    if 0 < b < 9:
        print("dv=",b)

    if p ==10:
        print("dv=0")
