#Nota final
print ("ingrese sus notas")
PT = float(input("ingrese notas de tarea: "))
pI = float(input("ingrese notas de interrogaciones: "))
NE = float(input("ingrese nota de examen: "))
PP = float(input("ingrese nota de presentacion: "))
NP = 0.3*PT+0.3*pI+0.3*NE+0.1*PP
print("la nota de presentacion es: ","{:.1f}".format(NP))
     