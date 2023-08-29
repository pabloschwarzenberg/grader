#Nota final
PT=float(input("Ingrese la nota de las tareas:"))
PI=float(input("Ingrese la nota de la Interrogacion:"))
NE=float(input("Ingrese la nota del examen:"))
PP=float(input("Ingrese la nota de la presentacion:"))
PF=((0.3 * PT) + (0.3 * PI) + (0.3 * NE) + (0.1 * PP))
NPF = round(PF, 1)
print(NPF)
     