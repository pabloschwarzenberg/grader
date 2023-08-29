#Nota final 
#Datos
PT=float(input("Ingrese la nota obtenida  tareas : "))
PI=float(input("Ingrese la nota obtenida  interrogacion : "))
NE=float(input("Ingrese la nota obtenida  examen : "))
pp=float(input("Ingrese la nota obtenida  presentacion : "))

#Procedimiento
resultado=0.3*PT+0.3*PI+0.3*NE+0.1*pp
print("La nota final seria",round(resultado,1))