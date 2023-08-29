PT = float(input("Ingrese la nota de las Tareas: "))
PI = float(input("Ingrese la nota de las Interrogaciones: "))
NE = float(input("Ingrese la nota del Examen: "))
PP = float(input("Ingrese la nota de Presentación: "))

prom= round((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP) , 1)


print("La nota final es: ", prom)
