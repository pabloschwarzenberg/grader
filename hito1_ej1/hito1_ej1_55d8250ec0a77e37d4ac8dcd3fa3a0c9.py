#Nota final
print("Ingrese las notas")

PT=float(input("Ingrese la nota de las tareas: "))
PI=float(input("Ingrese la nota de las interrogaciones: "))
NE=float(input("Ingrese la nota de las examen: "))
PP=float(input("Ingrese la nota de las presentacion: "))

PTF=PT * 0.3
PIF=PI * 0.3
NEF=NE*0.3
PPF=PP*0.1
RF=PTF+PIF+NEF+PPF
print("{0:.1f}".format(RF))