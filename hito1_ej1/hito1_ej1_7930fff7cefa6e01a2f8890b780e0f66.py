PT = input("Ingrese la nota de las Tareas (PT): ")
PI = input("Ingrese la nota de las Interrogaciones (PI): ")
NE = input("Ingrese la nota del Examen (NE): ")
PP = input("Ingrese la nota de la Presentación (PP): ")

PT = float(PT)
PI = float(PI)
NE = float(NE)
PP = float(PP)

promedio_final = (0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)

promedio_final = round(promedio_final, 1)

print("El promedio final es:", promedio_final)