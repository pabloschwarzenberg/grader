#Nota final
PT=float(input(" Ingrese el promedio de tareas: "))
PI=float(input(" Ingrese el primedio de interrogaciones: "))
NE=float(input(" Ingrese la nota del examen: "))
PP=float(input(" Ingrese la nota de presentación"))

Nota=0.3*PT+0.3*PI+0.3*NE+0.1*PP
print("La nota final es: ", round(Nota,1))

     