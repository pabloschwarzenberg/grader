#Sistema de Ecuaciones
#ax+by=c
#dx+ey=f
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
#x=(c-by)/a
#y=(f-ey)/d
y=(a*f-d*c)/(a*e-d*b)
x=(c-b*y)/a
yy=round(y,1)
xx=round(x,1)
print("x=",xx)
print("y=",yy)