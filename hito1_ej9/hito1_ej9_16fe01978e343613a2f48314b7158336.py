#Sistema de Ecuaciones
a = float(input("Ingrese el coeficiente del x de la primera ecuacion:"))
b = float(input("Ingrese el coeficiente del y de la primera ecuacion:"))
c = float(input("Ingrese el resultado de la primera ecuacion:"))
d = float(input("Ingrese el coeficiente del x de la segunda ecuación:"))
e = float(input("Ingrese el coeficiente del y de la segunda ecuación:"))
f = float(input("Ingrese el resultado de la segunda ecuacion:"))
det = a*e - b*d
if det != 0:
     x = (e * c - b * f) / det
     y = (a * f - d * c) / det
     solucion1 = round(x,1)
     solucion2 = round(y,1)
     print("x=",solucion1,"y=",solucion2)
else:
     print("El sistema tiene infinitas soluciones o no tiene ninguna")

 