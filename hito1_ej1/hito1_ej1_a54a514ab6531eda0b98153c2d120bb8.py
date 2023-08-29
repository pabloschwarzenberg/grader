#Nota final
PT=float(input("nota de tareas: "))
PI=float(input("nota de interrogaciones: "))
NE=float(input("nota de examen: "))
PP=float(input("nota de presentacion: "))
PPT=0.3*PT
PPI=0.3*PI
PNE=0.3*NE
PPP=0.1*PP
Promediofinal=PPT+PPI+PNE+PPP
print(round(Promediofinal, 1))