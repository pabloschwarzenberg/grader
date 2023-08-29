#Nota final
import math
pt = eval(input("Ingrese tareas"))
pi = eval(input("Ingrese interrogaciones"))
ne = eval(input("Ingrese examen"))
pp = eval(input("Ingrese presentacion"))
promediofinal = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
promediofinal = promediofinal * 10
promediofinal = math.ceil(promediofinal)
promediofinal = promediofinal / 10
print(promediofinal)