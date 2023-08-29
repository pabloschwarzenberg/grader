#Nota final
#Nota Final
#Entradas
PT = float(input("Ingrese Nota de Tareas: "))
PI = float(input("Ingrese Nota de Interrogaciones: "))
NE = float(input("Ingrese Nota de Examen: "))
PP = float(input("Ingrese Nota de Presentación: "))

#Procesos
promedio = round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1)

print(promedio) 