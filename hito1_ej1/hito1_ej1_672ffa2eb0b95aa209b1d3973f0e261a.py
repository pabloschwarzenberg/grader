#Nota final
PT = float(input("ingrese la nota de tareas: "))
PI = float(input("ingrese la nota de interrogaciones: "))
NE = float(input("ingrese la nota de examen: "))
PP = float(input("ingrese la nota de presentacion: "))

NF1 = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
NF2 = round(NF1,1)
print("la nota final es :",NF2)
