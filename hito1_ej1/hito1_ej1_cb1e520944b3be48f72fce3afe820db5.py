#Nota final
import random
import math
pt=float(input('tareas: '))
pi=float(input('interrogaciones: '))
ne=float(input('nota examen: '))
pp=float(input('presentacion: '))
nota=0.3*pt+0.3*pi+0.3*ne+0.1*pp
nr=round(nota,1)
print('redondeado a un decimal: ',nr)
