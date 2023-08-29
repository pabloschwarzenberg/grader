#Nota final
PT = float(input("Ingrese la nota de sus tareas: "))
PI = float(input("Ingrese la nota de sus interrogaciones: "))
NE = float(input("Ingrese la nota de su examen: "))
PP = float(input("Ingrese la nota de presentacion: "))

x = (0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
print("Nota final: ",x)