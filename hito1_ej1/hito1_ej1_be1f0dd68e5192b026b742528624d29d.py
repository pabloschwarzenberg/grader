#Nota final
PT = float(input("Ingrese la nota final de su Tareas: "))
PI = float(input("Ingrese la nota final de sus Interrogaciones: "))
NE = float(input("Ingrese la nota final de sus Examenes: "))
PP = float(input("Ingrese la nota final de sus Presentaciones: "))

promedio = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
print(promedio)