#Nota final
PT=float(input("Ingrese nota de tareas: "))
PI=float(input("Ingrese nota de interrogaciones: "))
NE=float(input("Ingrese nota de examen: "))
PP=float(input("Ingrese nota de presentación: "))
promedio=round((0.3*PT+0.3*PI+0.3*NE+0.1*PP),1)
print("El promedio final es",promedio)