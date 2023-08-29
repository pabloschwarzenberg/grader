#Nota final
pt = float(input("su nota de tareas: "))
pi = float(input("su nota en interrogaciones: "))
ne = float(input("su nota en examen: "))
pp = float(input("su nota en presentacion: "))
 
p = (0.3 * pt + 0.3 * pi + 0.3 * ne + 0.1 * pp)
p = round(p,1)
print("Su promedio final es de: ", p)