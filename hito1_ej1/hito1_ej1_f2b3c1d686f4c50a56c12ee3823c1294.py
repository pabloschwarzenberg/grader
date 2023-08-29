#Nota final
PT = float(input("Ingrese la nota de tareas:")) 
PI = float(input("Ingrese la nota de interrogaciones:"))
NE = float(input("Ingrese la nota de examen:"))
PP = float(input("Ingrese la nota de presentación:"))

prom =(0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
PROM = round(prom, 1)
print("El promedio de las notas es:", PROM)
