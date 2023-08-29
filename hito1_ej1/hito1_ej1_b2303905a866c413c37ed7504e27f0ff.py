#Nota final
PT=float(input("Ingrese la nota de tareas: "))
PI=float(input("Ingrese la nota de interrogaciones: "))
NE=float(input("Ingrese la nota del exámen: "))
PP=float(input("Ingrese la nota de presentación: "))
nota=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round((nota), 1))     