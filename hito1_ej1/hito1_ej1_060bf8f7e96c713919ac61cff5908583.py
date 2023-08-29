pt=float(input('Tareas'))
pi=float(input('Interrogaciones'))
ne=float(input('Examen'))
pp=float(input('Presentacion'))

promedio=((0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp))
pr=round(promedio,1)
print(pr)