#Sistema de Ecuaciones
a1=float(input())
b1=float(input())
c1=float(input())
a2=float(input())
b2=float(input())
c2=float(input())
x=(c1-(b1*(a2*c1 - a1*c2)/(a2*b1 - a1*b2)))/a1
y=(a2*c1 - a1*c2)/(a2*b1 - a1*b2)
print("x=",round(x,1))
print("y=",round(y,1))