#Nota final
pt = float(input("Ingresa tu nota por tareas: "))
pi = float(input("Ingresa tu nota por interrogaciones: "))
ne = float(input("Ingresa tu nota por examenes: "))
pp = float(input("Ingresa tu nota por presentaciones: "))
promedio_final = (0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp)
print("Su promedio final es: ",round(promedio_final,2))