#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio, 1)

# Solicitar las notas al usuario
PT = float(input("Ingresa la nota de Tareas (PT): "))
PI = float(input("Ingresa la nota de Interrogaciones (PI): "))
NE = float(input("Ingresa la nota de Examen (NE): "))
PP = float(input("Ingresa la nota de Presentación (PP): "))

# Calcular el promedio final
promedio_final = calcular_promedio_final(PT, PI, NE, PP)

# Imprimir el resultado
print("El promedio final es:", promedio_final)
      