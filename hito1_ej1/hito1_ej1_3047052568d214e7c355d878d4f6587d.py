#Nota final
PT=float(input("ingrese el promedio de sus tareas: "))
PI=float(input("ingrese el promedio de sus interrogaciones: "))
NE=float(input("ingrese la nota del examen: "))
PP=float(input("ingrese la nota de presentacion : "))
calculapromedio=round((0.3*PT)+(0.3*PI)+(0.3*NE)+(0.1*PP),1)
print("el promedio es ",calculapromedio)      