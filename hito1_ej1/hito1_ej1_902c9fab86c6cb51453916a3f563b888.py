#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)

PT = float(input("Ingresa la nota de Tareas (PT): "))
PI = float(input("Ingresa la nota de Interrogaciones (PI): "))
NE = float(input("Ingresa la nota de Examen (NE): "))
PP = float(input("Ingresa la nota de Presentacion (PP): "))

promedio = calcular_promedio_final(PT, PI, NE, PP)
print("El promedio final es:", promedio)