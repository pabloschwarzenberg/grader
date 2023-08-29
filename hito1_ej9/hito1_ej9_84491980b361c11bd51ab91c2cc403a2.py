#Sistema de Ecuaciones
#ax+by+c dx+ey+f  x=(-by-c)/a
a=int(input("Ingrese el valor de a:"))
b=int(input("Ingrese el valor de b:"))
c=int(input("Ingrese el valor de c:"))
d=int(input("Ingrese el valor de d:"))
e=int(input("Ingrese el valor de e:"))
f=int(input("Ingrese el valor de f:"))
y=(d*c-a*f)/((d*b)-(a*e))
x=(c*e-b*f)/((a*e)-(d*b))
print("x=",x,"y=",y)  