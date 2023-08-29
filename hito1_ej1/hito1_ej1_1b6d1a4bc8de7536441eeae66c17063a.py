#Nota final
PT=float(input("Nota tareas: "))
PI=float(input("Nota interrogaciones: "))
NE=float(input("Nota examen: "))
PP=float(input("Nota presentacion: "))
PPT=0.3*PT
PPI=0.3*PI
PNE=0.3*NE
PPP=0.1*PP
Promedio=PPT+PPI+PNE+PPP
print(round(Promedio, 1))      