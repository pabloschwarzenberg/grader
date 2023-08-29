#Nota final
pt = float(input("Ingrese Notas Tareas (Ej:7.0) : "))
pi = float(input("Ingrese Notas Interrogaciones (Ej:7.0) : "))
ne = float(input("Ingrese Notas Examenes (Ej:7.0) : "))
pp = float(input("Ingrese Notas Presentacion (Ej:7.0) : "))

promedio = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)
print("Tu promedio Final es: {0:.1f}".format(promedio))