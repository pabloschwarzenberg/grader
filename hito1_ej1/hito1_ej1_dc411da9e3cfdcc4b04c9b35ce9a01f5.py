#Nota final
PT=float(input("Nota de tareas: "))
PI=float(input("Nota de interrogaciones: "))
NE=float(input("Nota de examen: "))
PP=float(input("Nota de presentacion: "))
PPT=0.3*PT
PPI=0.3*PI
PNE=0.3*NE
PPP=0.1*PP
PromedioFinal=PPT+PPI+PNE+PPP
print(round(PromedioFinal, 1))