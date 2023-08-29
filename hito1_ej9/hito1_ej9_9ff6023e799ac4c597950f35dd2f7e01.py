#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

y=((a*f)-(d*c))/((a*e)-(d*b))
x=((c*e)-(b*f))/((a*e)-(b*d))

print("x="+str(x))
print("y="+str(y))