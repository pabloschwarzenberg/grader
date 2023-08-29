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
#x=(f-ey)/d
y=(a*f-d*c)/(a*e-d*b)
x=(c-b*y)/a
y_=round(y,1)
x_=round(x,1)
print("x= ",x_)
print("y= ",y_)