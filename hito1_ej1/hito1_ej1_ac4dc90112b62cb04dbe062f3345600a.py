#Nota final
PT=float(input("Nota de tareas: "))
PT=round(PT,1)
PI=float(input("Nota de interrogaciones: "))
PI=round(PI,1)
NE=float(input("Nota de examen: "))
NE=round(NE,1)
PP=float(input("Nota de Presentaciones: "))
PP=round(PP,1)
PF=(0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP)%4
PF=round(PF,1)
print(PF)