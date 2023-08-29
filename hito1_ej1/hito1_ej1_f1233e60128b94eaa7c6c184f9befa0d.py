#Nota final

pt = float(input("Ingrese la nota de las Tareas: "))
pi = float(input("Ingrese la nota de las Interrogaciones: "))
ne = float(input("Ingrese la nota del Examen: "))
pp = float(input("Ingrese la nota de la Presentacion: "))

promedio_final = 0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp

print("El promedio final es:", round(promedio_final, 1))
      