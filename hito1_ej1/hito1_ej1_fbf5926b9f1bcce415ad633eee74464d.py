#Nota final
print("Tareas:")
PT = float(input("ingrese Tarea:"))
PI = float(input("Ingrese Interrogación:"))
NE = float(input("Ingrese Examen:"))
PP = float(input("Ingrese Presentación:"))
Promedio = float((0.3 * PT)+( 0.3 * PI) +(0.3 * NE) + (0.1 * PP))
print (round(Promedio,1))