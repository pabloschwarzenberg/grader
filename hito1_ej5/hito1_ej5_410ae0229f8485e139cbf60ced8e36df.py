#Cálculo del dígito verificador de un rut
rut=int(input())
A=(rut//10**7)
a=((rut//10**6)%10)
b=((rut//10**5)%10)
c=((rut//10**4)%10)
d=((rut//10**3)%10)
e=((rut//10**2)%10)
f=((rut//10**1)%10)
g=(rut%10)
g1=g*2
f1=f*3
e1=e*4
d1=d*5
c1=c*6
b1=b*7
a1=a*2
A1=A*3
x=((a1+b1+c1+d1+e1+f1+g1+A1)%11)
y=(11-x)
if 0<=y<=9:
    print("dv=",y)
elif y==10:
    print("dv=k")
else:
    print("dv=0")