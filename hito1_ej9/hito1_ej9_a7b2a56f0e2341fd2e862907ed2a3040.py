#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

x=(((c*e)-(b*f))/((e*a)-(b*d)))
y=(((a*f)-(d*c))/((a*e)-(d*b)))

print("x=",(float(x)))
print("y=",(float(y)))    