#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
    return round(promedio_final, 1)

#Solicitar al usuario ingresar las cuatro notas
PT = float(input("Ingrese la nota de Tareas (PT): "))
PI = float(input("Ingrese la nota de Interrogaciones (PI): "))
NE = float(input("Ingrese la nota de Examen (NE): "))
PP = float(input("Ingrese la nota de Presentación (PP): "))

#Calcular el promedio final
promedio = calcular_promedio_final(PT, PI, NE, PP)

#Imprimir el resultado
print("El promedio final es:", promedio)