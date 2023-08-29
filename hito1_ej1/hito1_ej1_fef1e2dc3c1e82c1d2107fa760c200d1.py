#Nota final
PT=float(input("Ingresa tu nota de Tarea"))
PI=float(input("Ingresa tu nota de Interrogaciones"))
NE=float(input("Ingresa tu nota de Examen"))
PP=float(input("Ingresa tu nota de Presentacion"))

PF= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
PF=round(PF, 1)
print(PF)
