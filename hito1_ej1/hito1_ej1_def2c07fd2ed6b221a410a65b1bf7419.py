#Nota final
PT=float(input("Tareas: "))
PI=float(input("Interrogaciones: "))
NE=float(input("Examen: "))
PP=float(input("Presentacion: "))
NP=0.3*PT+0.3*PI+0.3*NE+0.1*PP
NF=round(NP,1)
print(NF)