#Nota final
pt = float(input("Introduce la nota de Tareas (PT): "))
pi = float(input("Introduce la nota de Interrogaciones (PI): "))
ne = float(input("Introduce la nota de Examen (NE): "))
pp = float(input("Introduce la nota de Presentación (PP): "))
# Calculamos el promedio final
promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
# Imprimimos el promedio final redondeado a un decimal
print("El promedio final es:", round(promedio, 1))
   