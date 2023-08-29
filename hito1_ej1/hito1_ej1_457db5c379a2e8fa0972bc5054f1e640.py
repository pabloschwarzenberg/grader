#Nota final
PT=float(input("Ingresa nota de Tareas: "))
PI=float(input("Ingresa nota de Interrogaciones: "))
NE=float(input("Ingresa nota de Examen: "))
PP=float(input("Ingresa nota de Presentación: "))
PF= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
Pff=round(PF,1)
print(Pff)