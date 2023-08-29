#Nota final
print("ingrese sus notas")
PT = float(input("ingrese la nota de las tareas: "))
PI = float(input("ingrese la nota de las interrogaciones: "))
NE = float(input("ingrese la nota del Examen: "))
PP = float(input("ingrese la nota de la presentacion: "))
promedio= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
print("promedio final" ,round(promedio,1))