#Nota final
PT=float(input("Ingrese nota tarea: "))
PI=float(input("Ingrese nota ies: "))
NE=float(input("Ingrese nota examen: "))
PP=float(input("Ingrese nota presentacion: "))

prom=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(round(prom,1))      