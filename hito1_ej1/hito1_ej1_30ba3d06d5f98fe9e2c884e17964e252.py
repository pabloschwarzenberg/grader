#Nota final
 
PT = float(input("Ingrese nota de tareas"))
PI = float(input("ingrese nota de interrogaciones"))
NE = float(input("ingrese nota de examen"))
PP = float(input("ingrese nota de presentacion"))

Promedio_final =((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP))

print("{0:.1f}".format(Promedio_final))      