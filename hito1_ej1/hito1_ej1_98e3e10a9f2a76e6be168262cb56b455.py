#Nota final
pt = float(input("Ingrese su nota de tareas: "))
pi = float(input("Ingrese su nota de interrogaciones: "))
ne = float(input("Ingrese su nota de examen: "))
pp = float(input("Ingrese su nota de presentacion: "))

p = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
pf = round(p,1)

print("Su promedio final es de: ",pf)      