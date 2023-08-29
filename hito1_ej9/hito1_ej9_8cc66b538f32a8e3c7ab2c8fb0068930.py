#Sistema de Ecuaciones
print("ax+by=c")
print("dx+ey=f")

a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
d=float(input("d= "))
e=float(input("e= "))
f=float(input("f= "))

y=((c*d-a*f)//(b*d-a*e))
print("y=",str(y))
x=((c*e-b*f)//(a*e-b*d))
print("x=",str(x))