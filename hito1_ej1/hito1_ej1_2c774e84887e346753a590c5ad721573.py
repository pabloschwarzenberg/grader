#Nota final
PT = float(input("ingrese nota tareas: "))
PI = float(input("ingrese nota interogantes: "))
NE = float(input("ingrese nota examen: "))
PP = float(input("ingrese nota presentacion: "))

PF = round((0.3PT + 0.3PI + 0.3NE + 0.1PP),1)

print("nota final es :", PF)