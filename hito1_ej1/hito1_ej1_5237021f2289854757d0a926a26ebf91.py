#Nota final
PT = eval(input("Ingrese nota Tareas: "))
PI = eval(input("Ingrese nota Interrogaciones: "))
NE = eval(input("Ingrese nota Examen: "))
PP = eval(input("Ingrese nota Presentacion: "))

prom = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print(round(prom, 1))