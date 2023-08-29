#Nota final
PT=float(input("Ingrese la Nota de Tareas:"))
PI=float(input("Ingrese la Nota de Interrogaciones:"))
NE=float(input("ingrese la Nota del Examen:"))
PP=float(input("ingrese la nota de Presentación:"))

promedio=0.3*PT+0.3*PI+0.3*NE+0.1*PP

Notafinal=round(promedio,1)

print("El Promedio Final es:",Notafinal)