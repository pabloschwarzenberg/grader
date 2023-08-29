#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio_final, 1)

# Solicitar al usuario las notas
nota_PT = float(input("Ingresa la nota de Tareas (PT): "))
nota_PI = float(input("Ingresa la nota de Interrogaciones (PI): "))
nota_NE = float(input("Ingresa la nota de Examen (NE): "))
nota_PP = float(input("Ingresa la nota de Presentación (PP): "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(nota_PT, nota_PI, nota_NE, nota_PP)

# Imprimir el resultado
print("El promedio final es:", promedio_final)
      