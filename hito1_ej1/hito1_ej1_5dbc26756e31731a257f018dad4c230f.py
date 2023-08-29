#Nota final
import math
pt = eval(input("ingrese tareas"))
pi = eval(input("ingrese interrograciones"))
ne = eval(input("ingrese examenes"))
pp = eval(input("ingrese presentaciones"))
promedioFinal = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
promedioFinal = promedioFinal*10
promedioFinal = math.ceil(promedioFinal)
promedioFinal = promedioFinal / 10
print(promedioFinal)