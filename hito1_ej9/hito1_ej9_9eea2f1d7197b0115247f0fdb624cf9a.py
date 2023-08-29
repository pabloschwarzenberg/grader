#Sistema de Ecuaciones
print("Resolviendo")
print("ax+by=c")
print("dx+ey=f")

a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
d=float(input("d= "))
e=float(input("e= "))
f=float(input("f= "))

y=(f-(d*c/a))/(e-(d*b/a))
x=((c-b*y)/a)

print("x=", x)
print("y=", y)
 