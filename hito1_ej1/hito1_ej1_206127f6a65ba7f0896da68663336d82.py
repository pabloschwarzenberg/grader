#Nota final
PT = float(input("introducir nota de las tareas: "))
PI = float(input("introducir nota de las interrogaciones: "))
NE = float(input("introducir nota del examen: "))
PP = float(input("introducir nota de la presentacion: "))
promedio = 0
promedio = (PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1)

print(round(promedio,1))