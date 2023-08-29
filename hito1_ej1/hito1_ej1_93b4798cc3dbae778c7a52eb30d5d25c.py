#Nota final
PT=float(input("Nota de Tareas:"))
PI=float(input("Nota de Interrogaciones:"))
NE=float(input("Nota de Examen:"))
PP=float(input("Nota de Presentacion:"))

NF=round(0.3*PT+0.3*PI+0.3*NE+0.1*PP,1)
print(NF)
      