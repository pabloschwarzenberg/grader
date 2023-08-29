#Nota final
PT = float(input("ingrese nota tareas: "))
PI = float(input("ingrese nota interogantes: "))
NE = float(input("ingrese nota examen: "))
PP = float(input("ingrese nota presentacion: "))

PF = round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1)

print("nota final es :", PF)