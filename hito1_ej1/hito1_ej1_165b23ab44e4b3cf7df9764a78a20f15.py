#Nota final
print("Calcularemos el promedio de un alumno con 4 notas")
PT=float(input("Ingresa la nota de las tareas: (PT) "))
PI=float(input("Ingresa la nota de las interrogaciones: (PI) "))
NE=float(input("Ingresa la nota del examen: (NE) "))
PP=float(input("Ingresa la nota de la presentación: (PP) "))
f=(0.3*PT)+(0.3*NE)+(0.1*PP)+(0.3*PI)
print("Su promedio es de ",round(f,1))