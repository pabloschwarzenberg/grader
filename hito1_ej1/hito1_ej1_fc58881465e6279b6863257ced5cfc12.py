#Nota final
pt = float(input("Ingrese nota de tareas: "))
pi = float(input("Ingrese nota de interrogaciones: "))
ne = float(input("Ingrese nota de examen: "))
pp = float(input("Ingrese nota de presentación: "))

promedio = (pt*0.3+pi*0.3+ne*0.3+pp*0.1)

print("El promedio es: ")
print(round(promedio,1))
