pt = float(input("Ingrese el promedio de tareas: "))
pi = float(input("Ingrese el promedio de interrogaciones: "))
ne = float(input("Ingrese el promedio de examenes: "))
pp = float(input("Ingrese el promedio de presentaciones: "))

promedio = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)

print(round(promedio, 1))