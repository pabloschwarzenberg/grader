#Nota final
import math
pt=eval(input("Ingrese tareas"))
pi=eval(input("Ingrese interrogaciones"))
ne=eval(input("Ingrese examen"))
pp=eval(input("Ingrese presentacion"))
promedioFinal=0.3*pt + 0.3*pi + 0.3*ne +0.1*pp
promedioFinal=promedioFinal * 10
promedioFinal=math.ceil(promedioFinal)
promedioFinal=promedioFinal / 10
print(promedioFinal)  