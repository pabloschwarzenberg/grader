pt = float(input("Ingrese la nota de la Tarea: "))
pi = float(input("Ingrese la nota de la Interrogacion: "))
ne = float(input("Ingrese la nota del Examen: "))
pp = float(input("Ingrese la nota de la Presentacion: "))

promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print("Estimado usuario su promedio final es: ", round(promedio,1))