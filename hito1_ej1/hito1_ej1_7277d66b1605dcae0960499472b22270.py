#Nota final
def calcular_promedio(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio, 1)

PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de Examen: "))
PP = float(input("Ingrese la nota de Presentacion: "))

promedio_final = calcular_promedio(PT, PI, NE, PP)
print("El promedio final es:", promedio_final)      