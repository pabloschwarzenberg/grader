#Nota final
#Definir notas
PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de presentación: "))
#Calculo y Print
promedio_final = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
print(round(promedio_final, 1))
     