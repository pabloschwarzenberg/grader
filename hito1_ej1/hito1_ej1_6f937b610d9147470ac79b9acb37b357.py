#Nota final
PT=float(input("Introducir promedio de tareas: "))
PI=float(input("Introducir promedio de interrogaciones: "))
NE=float(input("Introducir nota de examen: "))
PP=float(input("Introducir nota de presentación: "))
PF= 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP
print("El promedio final es: {}".format(PF))