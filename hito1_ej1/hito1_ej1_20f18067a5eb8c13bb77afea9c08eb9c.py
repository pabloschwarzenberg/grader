#Nota final
PT=float(input("Ingrese nota de tarea:"))
PI=float(input("Ingrese nota de interrogación:"))
NE=float(input("Ingrese nota de examen:"))
PP=float(input("Ingrese nota de presentación:"))
promedio=0.3*PT+0.3*PI+0.3*NE+0.1*PP
Promedio=(round(promedio,1))
print(Promedio)