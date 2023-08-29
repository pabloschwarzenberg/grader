#Nota final
pt=float(input("Ingresa tu puntaje de tareas: "))
pi=float(input("Ingresa tu punraje en interrogaciones: "))
ne=float(input("Ingresa tu puntaje en examenes: "))
pp=float(input("ingresa tu nota en presentaciones: "))
promedio= 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
promedio_redondeado= round(promedio, 1)
print(promedio_redondeado)