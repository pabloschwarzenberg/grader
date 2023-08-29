#Nota final

PT=float(input("ingrese nota de la tarea: "))
PI=float(input("ingrese nota de interrogacion: "))
NE=float(input("ingrese nota de examen: "))
PP=float(input("ingresenota de presentacion: "))


PF= ((0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP))
PF= round(PF,1)

print("el promedio final redondeado es: ", (PF))