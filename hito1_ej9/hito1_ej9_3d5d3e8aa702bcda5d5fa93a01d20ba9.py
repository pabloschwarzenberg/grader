#Sistema de Ecuaciones
print("ax+by=c")
print("dx+ey=f")

a=float(input("Ingrese el valor de a= "))
b=float(input("Ingrese el valor de b= "))
c=float(input("Ingrese el valor de c= "))
d=float(input("Ingrese el valor de d= "))
e=float(input("Ingrese el valor de e= "))
f=float(input("Ingrese el valor de f= "))

x=(((b*f)-(c*e))/((-a*e)+(d*b)))
y=(((a*f)-(c*d))/((-b*d)+(a*e)))

print("x=",round(x,1))
print("y=",round(y,1))
