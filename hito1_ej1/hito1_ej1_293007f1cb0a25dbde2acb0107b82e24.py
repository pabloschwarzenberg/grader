#Nota final

print("Bienvenido, ingrese sus notas")

pt = eval(input("Ingrese nota de tareas: "))
pi = eval(input("ingrese nota de interrogaciones: "))
ne = eval(input("Ingrese nota de examen: "))
pp = eval(input("Ingrese nota de presentacion: "))

# Hoja de calculo

promedio = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)

# Desarrollo

print(round(promedio,1))