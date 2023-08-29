#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

x=(e*c)-(b*f)
x1=x/((a*e)-(b*d))

y=(a*f)-(d*c)
y1=y/((a*e)-(b*d))

print("x=",x1)
print("y=",y1)
