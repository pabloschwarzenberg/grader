#Nota final

PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota de exámen: "))
PP = float(input("Ingrese la nota de presentación: "))

a = round(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP / 4)

print("{0:.1f}".format(a))
