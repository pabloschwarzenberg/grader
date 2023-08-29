"""
12.- Escribe un programa que resuelva un sistema de dos ecuaciones con dos incognitas.
Tu programa recibirá los seis números reales que representan el sistema y deberá imprimir 
la dos soluciones redondeadas a un decimal. Ejemplo: Para el sistema 2x+3y=6 y x+2y=5,
tu programa debe imprimir
•	x=-3.0
•	y=4.0
"""

print("Ecuación 1:")
x1 = float(input("- Coeficiente de x: "))
y1 = float(input("- Coeficiente de y: "))
a1 = float(input("- Resultado: "))

print("\nEcuación 2:")
x2 = float(input("- Coeficiente de x: "))
y2 = float(input("- Coeficiente de y: "))
a2 = float(input("- Resultado: "))

"""Resolveremos el sistema utilizando el método de reducción o eliminación"""

#Primero multiplicamos la primera ecuación de modo que luego se elimine con la segunda.
if x1 < 0 and x2 < 0:
    multiplo = -x2/x1
elif x1 > 0 and x2 > 0:
    multiplo = -x2/x1
else:
    multiplo = x2/x1

#Nueva ecuación
x1 = x1*multiplo
y1 = y1*multiplo
a1 = a1*multiplo

#Sumamos la nueva ecuación multiplicada con la segunda ecuación obteniendo la ecuación 3
x3 = x1+x2
y3 = y1+y2
a3 = a1+a2

y = a3/y3

x = a1/x1 - (y1*y)/x1

print("\nx =", x)
print("y =", y)


     