#Datos
PT=float(input(" Ingrese la nota obtenida en las tareas : "))
PI=float(input(" Ingrese la nota obtenida en la interrogacion : "))
NE=float(input(" Ingrese la nota obtenida en el examen : "))
PP=float(input(" Ingrese la nota obtenida en la presentacion : "))
#Procedimiento
resultado=0.3*PT+0.3*PI+0.3*NE+0.1*PP
print(" La nota final seria",round(resultado,1))
