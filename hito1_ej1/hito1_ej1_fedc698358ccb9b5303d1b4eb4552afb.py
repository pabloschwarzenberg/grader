#Nota final
PT=float(input("ingresa nota tareas:"))
PI=float(input("ingresa nota interrogaciones:"))
NE=float(input("ingresa nota de examen:"))
PP=float(input("ingres nota de presentacion:"))
Promedio=0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
Promedio=round(Promedio,1)
print(Promedio)