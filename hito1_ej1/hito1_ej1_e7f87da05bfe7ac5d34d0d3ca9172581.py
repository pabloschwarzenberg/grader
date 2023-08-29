#Nota final
#Captura de Datos
pt = float(input("Indique calificación de tareas: "))
pi = float(input("Indique calificación de interrogaciones: "))
ne = float(input("Indique calificación de examen: "))
pp = float(input("Indique calificación de presentación: "))
#Proceso
nf = (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
#Salida
print("Nota Final:",round(nf,1))