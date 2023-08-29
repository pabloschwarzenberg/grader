#Nota final
PT = float(input("Nota de la Tarea (PT): "))
PI = float(input("Nota de la interrogacion (PI): "))
NE = float(input("Nota del Examen (NE): "))
PP = float(input("Nota de la Presentacion (PP): "))

promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print("El promedio final es:", round(promedio_final, 1))      