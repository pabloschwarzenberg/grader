pt = float (input("Ingrese nota de tareas"))
pi = float (input("Ingrese nota de Interrogaciones"))
ne = float (input("Ingrese nota de Examen"))
pp = float (input("Ingrese nota de Presentacion"))
promedio = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
promedio = round(promedio,1)
print(promedio)
