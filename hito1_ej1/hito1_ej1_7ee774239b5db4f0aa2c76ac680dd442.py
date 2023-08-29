#Nota final
pt = float(input("Ingresa la nota de Tareas: "))
pi = float(input("Ingresa la nota de Interrogaciones: "))
ne = float(input("Ingresa la nota de Examen: "))
pp = float(input("Ingresa la nota de Presentación: "))

# Calculamos el promedio final con la fórmula dada
promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

# Imprimimos el promedio final redondeado a un decimal
print (f "El promedio final es: {promedio:.1f} ")
