#Sistema de Ecuaciones
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

x=round((c*e-b*f)/(a*e-b*d),1)
y=round((f*a-d*c)/(a*e-b*d),1)

print("x="+str(x))
print("y="+str(y))
