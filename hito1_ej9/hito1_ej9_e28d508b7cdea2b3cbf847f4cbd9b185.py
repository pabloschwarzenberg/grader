#Sistema de Ecuaciones
#Ecuacion 1: ax+by=c
a=int(input())
b=int(input())
c=int(input())
#Ecuacion 2: hx+my=g
h=int(input())
m=int(input())
g=int(input())

y= (a*g-h*c)/(a*m-b*h)
x= (c-b*y)/a
print("x=",round(x,1))
print("y=",round(y,1))