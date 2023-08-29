#Nota final
PT=float(input("Promedio Tareas:"))
PI=float(input("Pomedio Interrogaciones:"))
NE=float(input("Nota Examen:"))
PP=float(input("Nota Presentacion:"))
NF=0.3*PT+0.3*PI+0.3*NE+0.1*PP
NF=round(NF,1)
Notafinal=print("Nota final:",NF)
    