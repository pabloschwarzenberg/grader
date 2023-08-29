#Nota final
# Solicitar las notas al usuario
PT = float(input("Ingrese la nota de Tareas (PT): "))
PI = float(input("Ingrese la nota de Interrogaciones (PI): "))
NE = float(input("Ingrese la nota de Examen (NE): "))
PP = float(input("Ingrese la nota de Presentación (PP): "))
#Calcular promedio dada la formula
def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)
# Calcular el promedio final
promedio_final = calcular_promedio_final(PT, PI, NE, PP)

# Mostrar el resultado
print("El promedio final es:", promedio_final)
      