#Nota final
PT=input("Ingrese la nota de Tareas: ")
PT=float(PT)
PI=input("Ingrese la nota de Interrogaciones: ")
PI=float(PI)
NE=input("Ingrese la nota de Examen: ")
NE=float(NE)
PP=input("Ingrese la nota de Presentacion: ")
PP=float(PP)
Promedio=(0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
Promedio=float(Promedio)
print(Promedio)