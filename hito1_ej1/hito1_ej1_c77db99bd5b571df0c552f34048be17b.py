#Nota final
PT = float(input("Ingrese nota de tarea:/n "))
PI = float(input("Ingrese nota de interrogación:/n "))
NE = float(input("Ingrese nota de examen:/n "))
PP = float(input("Ingrese nota de presentación:/n "))

Promedio = ((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP))

print("El promedio final es ->", round(Promedio, 1))