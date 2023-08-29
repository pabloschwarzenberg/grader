#Nota final

#Ingreso de datos

pt = float(input("Ingrese las notas de las Tareas: "))
pi = float(input("Ingrese las notas de las Interrogaciones: "))
ne = float(input("Ingrese la nota del Examen: "))
pp = float(input("Ingrese la nota de Presentacion: "))

# Operacion
prom = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

# Imprimir el resultado
print("El promedio final es:", round(prom, 1))