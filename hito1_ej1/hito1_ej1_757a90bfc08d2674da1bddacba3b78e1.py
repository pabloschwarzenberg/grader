#Nota final
PT = float(input("ingrese nota de tareas: "))
PI = float(input("ingrese nota de interrogaciones: "))
NE = float(input("ingrese nota del examen: "))
PP = float(input("ingrese nota de presentacion: "))
NF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
NF2 = round(NF, 1)
print("Su promedio final es: ",NF2)      