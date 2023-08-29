#Nota final
PT=float(input("ingrese la nota de tareas: "))
PI=float(input("ingrese la nota de interrogaciones: "))
NE=float(input("ingrese la nota del examen: "))
PP=float(input("ingrese la nota de la presentacion: "))
promedio=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
promedio=round(promedio,1)
print("el promedio de las notas es: ",promedio)