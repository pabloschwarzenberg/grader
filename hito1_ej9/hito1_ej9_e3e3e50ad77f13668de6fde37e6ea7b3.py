#Sistema de Ecuaciones
a= float(input("ingrese valor de a:"))
b= float(input("ingrese valor de b:"))
c= float(input("ingrese valor de c:"))
d= float(input("ingrese valor de d:"))
e= float(input("ingrese valor de e:"))
f= float(input("ingrese valor de f:"))
det = a * e - b * d
if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det
    print("La solucion al sistema es x= %d e y= %d" % (x, y))
else :
    m = d / a
    if m * c == f :
        print ("El sistema tiene infinitas soluciones")
    else:
        print ("El sistema no tiene soluciones")