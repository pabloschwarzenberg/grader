#Nota final
# Pedimos al usuario que introduzca las notas
2
pt = float(input("Introduce la nota de Tareas (PT): "))
3
pi = float(input("Introduce la nota de Interrogaciones (PI): "))
4
ne = float(input("Introduce la nota de Examen (NE): "))
5
pp = float(input("Introduce la nota de Presentación (PP): "))
6
 
7
# Calculamos el promedio final
8
promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
9
 
10
# Imprimimos el promedio final redondeado a un decimal
11
print("El promedio final es:", round(promedio, 1))