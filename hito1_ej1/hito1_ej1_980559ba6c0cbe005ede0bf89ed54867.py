#Nota final
pt = float(input('Ingrese la nota de tarea \n'))
pi = float(input('Ingrese la nota de interrogacion \n'))
ne = float(input('Ingrese la nota de examen \n'))
pp = float(input('Ingrese la nota de presentacion \n'))

nf = (0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp)
print(round(nf,1))