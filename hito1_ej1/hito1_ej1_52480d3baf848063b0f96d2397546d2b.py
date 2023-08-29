#Nota final
print("Ingresa tu nota de tareas")
pt = float(input())
print("Ingresa tu nota de interrogaciones")
pi = float(input())
print("Ingresa tu nota de examen")
ne = float(input())
print("Ingresa tu nota de presentacion")
pp = float(input())

pf = (0.3 * pt) + (0.3 * pi) + (0.3 * ne) + (0.1 * pp)

print("Tu nota final es de",pf)