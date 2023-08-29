#Nota final
pt = float(input("nota tareas:"))
pi = float(input("nota interrogacion:"))
ne = float(input("nota examen:"))
pp = float(input("nota presentacion:"))

promedio = (0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp)
print(round(promedio,1))