#Nota final
PT = float(input("Ingrese nota de tareas: "))
PI = float(input("Ingrese nota de interrogaciones: "))
NE = float(input("Ingrese nota del examen: "))
PP = float(input("Ingrese nota de presentacion: "))
prom = (0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)
promedio = round(prom, 1)
print(promedio)