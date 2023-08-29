#Nota final
def calcular_promedio_final(pt, pi, ne, pp):
    promedio = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp
    return round(promedio, 1)

# Solicitar las cuatro notas al usuario
nota_PT = float(input("Ingresa la nota de PT (Tareas): "))
nota_PI = float(input("Ingresa la nota de PI (Interrogaciones): "))
nota_NE = float(input("Ingresa la nota de NE (Examen): "))
nota_PP = float(input("Ingresa la nota de PP (Presentacion): "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(nota_PT, nota_PI, nota_NE, nota_PP)

# Mostrar el resultado
print("El promedio final es:", promedio_final)
      