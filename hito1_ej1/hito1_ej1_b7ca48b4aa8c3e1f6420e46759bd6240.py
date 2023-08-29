#Nota final
PT = float(input("ingrese nota de la tarea: "))
PI = float(input("ingrese nota de la interrogacion: "))
NE = float(input("ingrese nota del examen: "))
PP = float(input("ingrese nota de la presentacion: "))
promedio =(float((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)))
print("su promedio es", round(promedio,1))      