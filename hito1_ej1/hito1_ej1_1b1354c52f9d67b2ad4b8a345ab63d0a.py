#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)

PT = float(input("Ingrese la nota de las Tareas (0-100): "))
PI = float(input("Ingrese la nota de las Interrogaciones (0-100): "))
NE = float(input("Ingrese la nota del Examen (0-100): "))
PP = float(input("Ingrese la nota de la Presentacion (0-100): "))

promedio = calcular_promedio_final(PT, PI, NE, PP)

print("El promedio final es:", promedio)      