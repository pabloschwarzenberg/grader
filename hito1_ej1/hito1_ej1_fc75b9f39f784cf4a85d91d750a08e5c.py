#Nota final
PT=float(input("Ingrese notas de tareas: "))
PI=float(input("Ingrese notas de interrogaciones: "))
NE=float(input("Ingrese nota de examen: "))
PP=float(input("Ingrese nota de presentacion: "))

promedio = (0.3*PT+0.3*PI+0.3*NE+0.1*PP)

print("su promedio final es", round (promedio,1))