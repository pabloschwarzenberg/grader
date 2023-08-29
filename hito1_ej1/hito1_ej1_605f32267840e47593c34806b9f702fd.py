#Nota final
pt = float(input("Ingrese la nota total de sus tareas: "))
pi = float(input("Ingrese la nota total de sus interrigaciones: "))
ne = float(input("Ingrese la nota total de sus examen: "))
pp = float(input("Ingrese la nota total de sus presentaciones: "))
promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp
redondeado = round(promedio,1)
print(redondeado)