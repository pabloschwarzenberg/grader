#Nota final
PT=float(input("Ingrese promedio tareas :"))
PI=float(input("Ingrese promedio interrogacion :"))
NE=float(input("Ingrese nota del examen :"))
PP=float(input("Ingrese nota de presentacion :"))
m=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("Promedio final :",round(m,1))
