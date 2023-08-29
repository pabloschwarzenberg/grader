#Sistema de Ecuaciones
a1=int(input())
b1=int(input())
c1=int(input())
a2=int(input())
b2=int(input())
c2=int(input())
y=(c1*a2-c2*a1)/(b1*a2-b2*a1)
x=(c1*b2-c2*b1)/(a1*b2-a2*b1)
print("x=",round(x,1))
print("y=",round(y,1))

