#Nota final
PT=float(input("Ingrese la nota obtenida por tareas: "))
PI=float(input("Ingrese la nota obtenida por interrogaciones: "))
NE=float(input("Ingrese la nota obtenida por examen: "))
PP=float(input("Ingrese la nota obtenida por presentacion: "))
PRT=0.3*PT+0.3*PI+0.3*NE+0.1*PP
x=round(PRT)
print("El promedio final es: ", x)