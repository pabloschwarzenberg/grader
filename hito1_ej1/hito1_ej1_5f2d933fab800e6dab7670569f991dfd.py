#Nota final
PT = float(input("ingrese nota de tareas: "))
PI = float(input("ingrese nota de Interrogaciones: "))
NE = float(input("ingrese nota de Examen: "))
PP = float(input("ingrese nota de Presentacion: "))

prom = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
promedio = round(prom,1)

print(promedio)