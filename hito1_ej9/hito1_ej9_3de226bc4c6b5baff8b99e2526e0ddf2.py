#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

x=((c*e)-(b*f))/((a*e)-(d*b))
y=((a*f)-(d*c))/((a*e)-(d*b))

print("x=",round(x,1))
print("y=",round(y,1))    