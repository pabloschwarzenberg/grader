#Nota final
PT=input("Nota Tareas: ")
PT=float(PT)

PI=input("Nota Interrogaciones: ")
PI=float(PI)

NE=input("Nota Examen: ")
NE=float(NE)

PP=input("Nota Presentacion: ")
PP=float(PP)


PF=0.3*PT+0.3*PI+0.3*NE+0.1*PP
PF=round(PF,1)

print("Promedio Final: ",PF)
