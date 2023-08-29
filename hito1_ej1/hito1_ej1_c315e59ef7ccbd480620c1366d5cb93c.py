#Nota final
PT=float(input("Ingrese nota de las tareas: "))
PI=float(input("Ingrese nota de las interrogaciones: "))
NE=float(input("Ingrese nota de los de examen: "))
PP=float(input("Ingrese nota de las presentacion: "))
PPT=0.3*PT
PPI=0.3*PI
PNE=0.3*NE
PPP=0.1*PP
PromedioFinal=PPT+PPI+PNE+PPP
PromedioFinal=round(PromedioFinal, 1)
print("El promedio final es de: ", PromedioFinal)      