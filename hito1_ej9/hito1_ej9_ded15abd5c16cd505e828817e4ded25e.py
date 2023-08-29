#Sistema de Ecuaciones
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=int(input("d: "))
e=int(input("e: "))
f=int(input("f: "))

x=(b*f-e*c)/(b*d-a*e)
y=(a*f-d*c)/(a*e-d*b)

print("x=",x)
print("y=",y)    