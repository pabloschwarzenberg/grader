#Nota final
PT = float(input("Ingrese su nota de tareas: "))
PI = float(input("Ingrese su nota de interrogaciones: "))
NE = float(input("Ingrese su nota de examen: "))
PP = float(input("Ingrese su nota de presentacion: "))

PF =  ( PT * 0.3 + PI * 0.3 + NE * 0.3 + PP * 0.1)
print(round(PF, 1))