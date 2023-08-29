#Nota final
PT = float(input("ingrese la nota su nota de tareas: "))
PI = float(input("ingrese la nota su nota de interrogaciones: "))
NE = float(input("ingrese la nota su nota de examen: "))
PP = float(input("ingrese la nota su nota de presentación: "))
formula = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("el promedio final de las notas es {:.1f}".format(formula))