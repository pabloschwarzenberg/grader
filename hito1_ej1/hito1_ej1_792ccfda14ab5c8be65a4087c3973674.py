#Nota final
PT = float(input("Ingrese la nota de las tareas: "))
PI = float(input("Ingrese la nota de las interrogaciones: "))
NE = float(input("Ingrese la nota de los examenes: "))
PP = float(input("Ingrese la nota de las presentaciones: "))
promedio = PT * 0.3 + PI * 0.3 + NE * 0.3 + PP * 0.1
print(round(promedio, 2))