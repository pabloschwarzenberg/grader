#Nota final
PT = float(input("Ingrese las notas de tareas: "))
PI = float(input("Ingrese las notas de interrogaciones: "))
NE = float(input("Ingrese las notas de exámenes: "))
PP = float(input("Ingrese las notas de presentaciones: "))

x = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
x = round(x, 1)

print(x)