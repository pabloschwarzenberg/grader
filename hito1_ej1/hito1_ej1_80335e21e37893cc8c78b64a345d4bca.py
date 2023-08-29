#Nota final
pt = float(input("ingrese nota de tareas: "))
pi = float(input("ingrese nota de interrogaciones: "))
ne = float(input("ingrese nota de examen: "))
pp = float(input("ingrese nota de presentacion: "))

#formula
pf = (0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp)

#salida
print("su promedio final es: ",pf)