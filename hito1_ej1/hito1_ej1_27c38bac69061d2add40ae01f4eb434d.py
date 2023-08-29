#Nota final
PT=float(input("Ingrese el promedio de Tareas:"))
PI=float(input("Ingrese el promedio de Interrogaciones:"))
NE=float(input("ingrese el promedio del Examen:"))
PP=float(input("ingrese la nota de Presentación:"))
promedio=0.3*PT+0.3*PI+0.3*NE+0.1*PP
Notafinal=round(promedio,1)
print("El Promedio Final es:",Notafinal)