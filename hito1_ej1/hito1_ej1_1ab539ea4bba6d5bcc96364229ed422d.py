#Nota final
PT= float(input("Ingrese promedio de tareas: "))
PI= float(input("Ingrese promedio de interrogaciones: "))
NE= float(input("Ingrese nota de examen: "))
PP= float(input("Ingrese nota presentación: "))
PF= 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
D=round(PF, 2)
print("Tu promedio es:",D)