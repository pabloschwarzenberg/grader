#Nota final
PT = float(input("ingrese la nota de Tareas: "))
PI = float(input("ingrese la nota de Interrogaciones: "))
NE = float(input("ingrese la nota del Examen: "))
PP = float(input("ingrese la nota de Presentacion: "))
PF = round(PT*.3 + PI*.3 + NE*.3 + PP*.1 , 2)
print(PF)