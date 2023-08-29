#Nota final
PT=float(input("Promedio tareas: "))
PI=float(input("Promedio interrogaciones: ")) 
NE=float(input("Nota examen: ")) 
PP=float(input("Promedio presentación: "))
PF=round((0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP),1)
print(PF)