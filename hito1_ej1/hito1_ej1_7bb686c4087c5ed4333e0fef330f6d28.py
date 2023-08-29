#Nota final
a = float(input("ingrese nota tareas: " ))
b = float(input("ingrese nota interrogantes: " ))
c = float(input("ingrese nota examen: " ))
d = float(input("ingrese notapresentación: " ))

pt = 0.3
pi = 0.3
ne = 0.3
pp = 0.1

promedio = str(a*pt + b*pi + c*ne + d*pp)
print("EL promedio es: " + promedio)
