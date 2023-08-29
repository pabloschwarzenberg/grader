#Nota final
print("Ingrese la nota de Tareas: ")
PT = float(input(">>>"))
print(("\nIngrese la nota de Interrogaciones: "))
PI = float(input(">>>"))
print("\nIngrese la nota de Examen: ")
NE = float(input(">>>"))
print("\nIngrese la nota de Presentacion: ")
PP = float(input(">>>"))

promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

promedio_r = round(promedio, 1)

print("El promedio final es:", promedio_r)