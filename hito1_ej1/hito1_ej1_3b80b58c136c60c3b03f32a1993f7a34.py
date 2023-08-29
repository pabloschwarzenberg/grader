PT=float(input("Nota de tareas: "))
PI=float(input("Nota de interrogaciones: "))
NE=float(input("Nota de examen: "))
PP=float(input("Nota de presentacion: "))
PPT=0.3PT
PPI=0.3PI
PNE=0.3NE
PPP=0.1PP
PromedioFinal=PPT+PPI+PNE+PPP
print(round(PromedioFinal, 1))