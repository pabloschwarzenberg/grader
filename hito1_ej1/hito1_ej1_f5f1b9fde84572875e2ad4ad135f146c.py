#Nota final
PT = float(input("Ingresa tu nota de las Tareas: "))
PI = float(input("Ingresa tu nota en las Interrogaciones: "))
NE = float(input("Ingresa tu nota en el Examen: "))
PP = float(input("Ingresa tu nota en la Presentación: "))

Nota_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

print('Tu promedio final es:', round(Nota_final, 1))      