#Nota final

pt = float(input("Ingresa promedio de tareas: "))
pi = float(input("Ingresa promedio de interrogaciones: "))
ne = float(input("Ingresa nota de examen: "))
pp = float(input("Ingresa promedio de presentaciones: "))

promediofinal = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)
print("Tu promedio final es: ", round(promediofinal,1))
