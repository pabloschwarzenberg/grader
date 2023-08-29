#Sistema de Ecuaciones
a = int(input("Ingrese valor de a:"))
b = int(input("Ingrese valor de b:"))
c = int(input("Ingrese valor de c:"))
d = int(input("Ingrese valor de d:"))
e = int(input("Ingrese valor de e:"))
f = int(input("Ingrese valor de f:"))

det = a * e - b * d
x = (e * c - b * f) / det
y = (a * f - d * c) / det

print ("La solucion al sistema es: x=",x, "y=", y)
    
  