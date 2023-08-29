PT=float(input("Ingrese nota de tareas: "))
PI=float(input("Ingrese nota de interrogaciones: "))
NE=float(input("Ingrese nota de examen: "))
PP=float(input("Ingrese nota de presentacion: "))

NF=(0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("La nota de Promedio final es: ", round(NF,1))