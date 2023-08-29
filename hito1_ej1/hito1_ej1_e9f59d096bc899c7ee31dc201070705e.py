#Nota final
pt = float(input("tareas:"))
pi = float(input("Interrogatorio: "))
ne = float(input("Examen: "))
pp = float(input("presentación"))

promedio = (0.3 * pt + 0.3*pi + 0.3*ne + 0.1*pp) 
print("El promedio es:", round(promedio, 1))