#Nota final
print("Ingrese sus notas de 1.0 a 7.0")
PT = float(input("Ingrese nota de las tareas: "))
PI = float(input("Ingrese nota de las interrogaciones: "))
NE = float(input("Ingrese nota del examen: "))
PP = float(input("Ingrese nota de la presentacion: "))

Promedio_Final = (0.3 * PT)+(0.3 * PI)+(0.3 * NE)+(0.1 * PP)
print("El promedio de las 4 notas es: ", Promedio_Final)