#Nota final
PT=float(input("ingrese nota de las tareas: "))
PI=float(input("ingrese nota de las interrogaciones: "))
NE=float(input("ingrese nota del examen: "))
PP=float(input("ingrese nota de la presentacion: "))


PF= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print(PF)
resultado=round(PF,1)

print("Su promedio final es:", resultado)

     