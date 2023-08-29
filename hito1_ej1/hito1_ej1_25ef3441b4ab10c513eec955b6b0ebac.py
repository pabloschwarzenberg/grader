#Nota final
PT=float(input("Ingrese la nota correspondiente a Tareas: "))
PI=float(input("Ingrese la nota correspondiente a Interrogaciones: "))
NE=float(input("Ingrese la nota correspondiente al Exámen: "))
PP=float(input("Ingrese la nota correspondiente a Presentación: "))
PF=0.3*PT+0.3*PI+0.3*NE+0.1*PP
PF=round(PF, 1)
print("El promedio final es: ",PF)