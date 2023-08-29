#Nota final
import math
pt = eval(input("ingrese tareas"))
pi = eval(input("ingrese interrogaciones"))
ne = eval(input("ingrese examen")) 
pp = eval(input("ingrese presentacion"))
promedioFinal = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
promedioFinal = promedioFinal * 10
promedioFinal = math.ceil(promedioFinal)
promedioFinal = promedioFinal / 10 
print(promedioFinal)    