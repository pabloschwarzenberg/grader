#Nota final

PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogantes: "))
NE = float(input("Ingrese la nota de examen: "))
PP = float(input("Ingrese la nota de presentación: "))
promedio_final = round(0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP, 1)
print("Su promedio final es: ", promedio_final)