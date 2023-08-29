def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)

# Solicitar las puntuaciones al usuario
PT = float(input("Ingrese la puntuación total del examen: "))
PI = float(input("Ingrese la puntuación total de la tarea individual: "))
NE = float(input("Ingrese la puntuación total de la nota del estudiante: "))
PP = float(input("Ingrese la puntuación total de la participación en clase: "))

# Calcular el promedio final
promedio = calcular_promedio_final(PT, PI, NE, PP)

# Imprimir el resultado redondeado a un decimal
print("El promedio final es:", promedio)

      