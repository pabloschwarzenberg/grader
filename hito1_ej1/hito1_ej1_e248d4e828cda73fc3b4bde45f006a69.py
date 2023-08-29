#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)

PT = float(input("Ingrese la nota de las tareas (PT): "))
PI = float(input("Ingrese la nota de las interrogaciones (PI): "))
NE = float(input("Ingrese la nota del examen (NE): "))
PP = float(input("Ingrese la nota de la presentación (PP): "))

promedio = calcular_promedio_final(PT, PI, NE, PP)
print("El promedio final es:", promedio)      