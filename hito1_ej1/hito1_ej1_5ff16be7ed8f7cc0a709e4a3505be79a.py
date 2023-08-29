#Nota final
def calcular_promedio(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Solicitar al usuario ingresar las notas
pt = float(input("Ingrese la nota de PT (Tareas): "))
pi = float(input("Ingrese la nota de PI (Interrogaciones): "))
ne = float(input("Ingrese la nota de NE (Examen): "))
pp = float(input("Ingrese la nota de PP (Presentacion): "))

# Calcular el promedio final
promedio_final = calcular_promedio(pt, pi, ne, pp)

# Imprimir el resultado
print("El promedio final es:", promedio_final)