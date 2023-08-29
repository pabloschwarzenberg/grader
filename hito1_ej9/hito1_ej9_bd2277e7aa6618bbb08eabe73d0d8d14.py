#Sistema de Ecuaciones
#Obtener los coeficientes y los resultados del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b1 = float(input("ingrese el coeficiente 'b' de la primera ecuación: "))
c1 = float(input("Ingrese el resultado de la primera ecuaión: "))

a2 = float(input("Ingrese el coeficiente 'a' de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente 'b' de la segunda ecuación: "))
c2 = float(input("Ingrese el resultado de la segunda ecuación: "))

#Calcular las soluciones del sistema de ecuaciones 
det = a1 * b2 - a2 * b1

if det == 0:
    print("El sistema de ecuaciones no tiene solución.")
else:
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    print("x =", round(x, 1))
    print("y =", round(y, 1))
    