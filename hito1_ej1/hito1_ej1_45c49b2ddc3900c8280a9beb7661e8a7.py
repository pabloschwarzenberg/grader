#Nota final
PT=float(input("Digite nota de las tareas: "))
PI=float(input("Digite nota de las interroganciones: "))
NE=float(input("Digite nota del examen: "))
PP=float(input("Digite nota de la presentacion:"))
pf=round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1)
print("Promedio final ",pf)  