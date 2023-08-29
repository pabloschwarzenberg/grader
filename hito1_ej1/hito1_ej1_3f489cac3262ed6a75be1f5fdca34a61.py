#Nota final
PT=float(input("Introduzca nota de tareas:"))
PI=float(input("Introduzca nota de las interrogaciones:"))
NE=float(input("Introduzca nota del examen:"))
PP=float(input("Introduzca nota de la presentacion:"))
Promediofinal =((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP))
print("{0:.1f}",format(Promediofinal) )