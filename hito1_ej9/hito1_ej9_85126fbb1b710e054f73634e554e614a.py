#Sistema de Ecuaciones
print("ax+by=c")
print("dx+ey=f")

a =int(input("ingrese valor de a:"))
b =int(input("ingrese valor de b:"))
c =int(input("ingrese valor de c:"))
d =int(input("ingrese valor de d:"))
e =int(input("ingrese valor de e:"))
f =int(input("ingrese valor de f:"))

y=((f*a)-(c*d))/((a*e)-(b*d))
x=(f-(e*y))/d
print("x=", x)
print("y=", y)

