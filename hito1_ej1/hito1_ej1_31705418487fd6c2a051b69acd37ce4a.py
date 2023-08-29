#Nota final
pt = float(input("Ingresar nota de Tarea: "))
pi = float(input("Ingresar nota de Interrogación: "))
ne = float(input("Ingresar nota de Examen: "))
pp = float(input("Ingresar nota de Presentación: "))

promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
promedio = round(promedio, 1)
print("Su promedio final es: ", promedio)
