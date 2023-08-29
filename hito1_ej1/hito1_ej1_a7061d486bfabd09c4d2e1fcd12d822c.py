#Nota final
pt = float(input('ingrese la nota obtenida por tareas: '))
pi = float(input('ingrese la nota obtenida por interrogaciones: '))
ne = float(input('ingrese la nota obtenida en el examen: '))
pp = float(input('ingrese la nota de la presentación: '))

print(round((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp),1))