#Nota final
#Entrada.
PT = float(input("Ingrese la nota de tareas: "))
PI = float(input("Ingrese la nota de interrogaciones: "))
NE = float(input("Ingrese la nota del examen: "))
PP = float(input("Ingrese la nota de presentación: "))
#Procedimiento.
PF = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
PFF = round(PF,1)
#Salida.
print(PFF)     