#Nota final
PT=float(input("Nota Tareas: "))
PI=float(input("Nota Interrogaciones: "))
NE=float(input("Nota Examen: "))
PP=float(input("Nota Presentación: "))
a=float(0.3)
b=float(0.1)
promedio=a*PT+a*PI+a*NE+b*PP
promedio=round(promedio,1)
print(promedio)      