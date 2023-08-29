#Nota final

pt = eval(input("Ingrese promedio de sus tareas: "))
pi = eval(input("Ingrese promedio de tus interrogantes: "))
ne = eval(input("Ingrese promedio de tus examenes: "))
pp = eval(input("Ingrese promedio de sus presentaciones: "))

promedio = (0.3)*pt + (0.3)*pi + (0.3)*ne + (0.1)*pp

r = round(promedio, 1)

print("Tu promedio es: ", r)