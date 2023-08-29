#Nota final
PT = float(input("Ingrese su nota de Tareas: "))
PI = float(input("Ingrese su nota de Interrogaciones: "))
NE = float(input("Ingrese su nota de Examen: "))
PP = float(input("Ingrese su nota de Presentacion: "))
Promedio_final = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
promedio_final = round(Promedio_final , 2)
print(promedio_final)
