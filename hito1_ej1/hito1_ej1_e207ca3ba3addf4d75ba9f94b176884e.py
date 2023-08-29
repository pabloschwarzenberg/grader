# Solicitar al usuario las cuatro notas
pt = float(input("Ingrese la nota de las Tareas (PT): "))
pi = float(input("Ingrese la nota de las Interrogaciones (PI): "))
ne = float(input("Ingrese la nota del Examen (NE): "))
pp = float(input("Ingrese la nota de la Presentacion (PP): "))

# Calcular el promedio final
promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

# Imprimir el resultado redondeado a un decimal
promedio_final_redondeado = round(promedio_final, 1)
print("El promedio final es:", promedio_final_redondeado)
