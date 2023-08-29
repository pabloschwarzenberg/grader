#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)
PT = float(input("Ingrese la nota de PT (Tareas): "))
PI = float(input("Ingrese la nota de PI (Interrogaciones): "))
NE = float(input("Ingrese la nota de NE (Examen): "))
PP = float(input("Ingrese la nota de PP (Presentacion): "))
promedio = calcular_promedio_final(PT, PI, NE, PP)
print("El promedio final es:", promedio)