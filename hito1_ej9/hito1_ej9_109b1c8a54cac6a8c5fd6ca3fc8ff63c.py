#Sistema de Ecuaciones
a1=int(input())
b1=int(input())
c1=int(input())
a2=int(input())
b2=int(input())
c2=int(input())

y=(a1*c2-a2*c1)/(-a2*b1+a1*b2)
x=(c1-b1*y)/a1
yr=round(y,1)
xr=round(x,1)

print("x=",xr)
print("y=",yr)
