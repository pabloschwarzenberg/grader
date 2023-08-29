#Nota final
NT = float(input("ingrese nota de la tarea:"))
NI = float(input("ingrese nota de la interrogacion:"))
NE = float(input("ingrese nota del examen:"))
NP = float(input("ingrese nota de la presentacion:"))
promedio=(0.3*NT + 0.3*NI + 0.3*NE + 0.1*NP)
print(round(promedio,1))
