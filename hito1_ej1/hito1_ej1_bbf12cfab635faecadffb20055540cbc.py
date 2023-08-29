import decimal
PT=float(input("Ingrese nota de tareas: "))
PI=float(input("Ingrese nota de interrogaciones: "))
NE=float(input("Ingrese nota de Examen: "))
PP=float(input("ingrese nota de Presentacion" ))
PF=(0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP)
print("El Promedio del alumno es: ", "{0:.1f}".format(PF))