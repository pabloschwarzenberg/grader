rut=str(input())
a=int(rut[0])
b=int(rut[1])
c=int(rut[2])
d=int(rut[3])
e=int(rut[4])
f=int(rut[5])
g=int(rut[6])
h=0
rut=int(rut)
if rut>9999999:
    rut=str(rut)
    h=int(rut[7])
    x=a*3+b*2+c*7+d*6+e*5+f*4+g*3+h*2
    y=x%11
    dv=11-y
else:
    x=a*2+b*7+c*6+d*5+e*4+f*3+g*2
    y=x%11
    dv=11-y

if dv==10:
    print("dv=k")
elif dv==11:
    print("dv=0")
else:
    dv=str(dv)
    print("dv="+dv)
