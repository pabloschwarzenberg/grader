#Función para obtener la nota promedio final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)
#Solicitar al usuario las notas
pt = float(input("Ingresa la nota de Tareas: "))
pi = float(input("Ingresa la nota de Interrogaciones: "))
ne = float(input("Ingresa la nota de Examen: "))
pp = float(input("Ingresa la nota de Presentación: "))
#Calcular el promedio final
promedio = calcular_promedio_final(pt, pi, ne, pp)
#Imprimir el resultado
print("El promedio final es:", promedio)