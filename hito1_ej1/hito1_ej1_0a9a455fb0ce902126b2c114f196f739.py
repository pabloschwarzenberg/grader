#Nota final

pt = float(input("Ingrese su nota por Tareas: "))
pi = float(input("Ingrese su nota por Interrogaciones: "))
ne = float(input("Ingrese su nota por Examen: "))
pp = float(input("Ingrese su nota por Presentacion: "))

promedio_final =  0.3*pt+0.3*pi+0.3*ne+0.1*pp

print(round(promedio_final,1))