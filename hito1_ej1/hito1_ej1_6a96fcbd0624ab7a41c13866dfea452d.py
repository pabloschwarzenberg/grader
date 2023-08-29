pt = float(input("Ingrese su nota de Tareas"))
pi = float(input("Ingrese su nota de Interrogaciones"))
ne = float(input("Ingrese su nota de Examen"))
pp = float(input("Ingrese su nota de Presentacion"))

promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
print(round(promedio, 1))
