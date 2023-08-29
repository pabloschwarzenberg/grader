#Nota final

PT=float(input("Nota de las Tareas: "))
PI=float(input("Nota de las Interrogaciones: "))
NE=float(input("Nota del Examen: "))
PP=float(input("Nota de Presentación: "))
NT=(0.3*PT+0.3*PI+0.3*NE +0.1*PP)
print("{0:.1f}".format(NT))