#Nota final
PT=float(input("Ingrese nota tareas: "))
PI=float(input("Ingrese nota interrogaciones: "))
NE=float(input("Ingrese nota examen: "))
PP=float(input("Ingrese nota presentacion: "))
promedio= round((0.3*PT+0.3*PI+0.3*NE+0.1*PP),1)
print("el promedio es de:",promedio)