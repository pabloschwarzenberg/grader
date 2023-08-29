#Nota final
PT = float(input("ingrese su promedio de tareas: "))
PI = float(input("ingrese su promedio de interrogaciones: "))
NE = float(input("ingrese su nota del examen: "))
PP = float(input("ingrese su promedio de presentaciones: "))

promedio_final = (0.3 * PT) + (0.3 * PI) + (0.3* NE) + (0.1 * PP)

promedio_final = round(promedio_final, 1)

print("El promedio final sería:", promedio_final)      