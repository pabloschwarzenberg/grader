#Nota final
PT = float(input("Ingrese la nota de Tareas: "))
PI = float(input("Ingrese la nota de Interrogaciones: "))
NE = float(input("Ingrese la nota de examenes: "))
PP = float(input("Ingrese la nota de presentacion: "))
PF = ((PT * 0.3) + (PI * 0.3) + (NE * 0.3) + (PP * 0.1))
PF1 = round(PF , 1)
print(PF1)    