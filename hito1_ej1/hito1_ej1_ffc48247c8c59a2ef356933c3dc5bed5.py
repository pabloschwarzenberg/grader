#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)

# Solicitar notas al usuario
PT = float(input("Ingresa la nota de Tareas: "))
PI = float(input("Ingresa la nota de Interrogaciones: "))
NE = float(input("Ingresa la nota de Examen: "))
PP = float(input("Ingresa la nota de Presentacion: "))

# Calcular el promedio final
promedio = calcular_promedio_final(PT, PI, NE, PP)

# Imprimir el resultado
print("El promedio final es:", promedio)
      