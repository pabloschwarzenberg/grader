#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio, 1)

#Ingrese las cuatro notas
PT = float(input("Ingresa la nota de las Tareas (PT): "))
PI = float(input("Ingresa la nota de las Interrogaciones (PI): "))
NE = float(input("Ingresa la nota del Examen (NE): "))
PP = float(input("Ingresa la nota de la Presentacion (PP): "))

#Calcular el promedio final
promedio_final = calcular_promedio_final(PT, PI, NE, PP)

print("El promedio final es:", promedio_final)
