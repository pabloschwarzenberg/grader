PT=float(input("Ingrese promedio de Tareas: "))
PI=float(input("Ingrese promedio de Interrogaciones: "))
NE=float(input("Ingrese nota de examen: "))
PP=float(input("Ingrese nota de presentación: "))

p=round((0.3*(PT+PI+NE))+0.1*PP,1)

print("El promedio es ",p)