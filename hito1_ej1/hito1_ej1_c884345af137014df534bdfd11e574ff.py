#Nota final
print("Ingrese Notas:\n")
PT = float(input("Ingrese Nota de Tareas:"))
PI = float(input("Ingrese Nota de Intenrogaciones:"))
NE = float(input("Ingrese Nota de Examen:"))
PP = float(input("Ingrese Nota de Presentacion:"))

Promedio = (PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1)

print(Promedio)  