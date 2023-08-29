#Nota final
print("A continuacion ingresa las notas requeridas para sacar tu promedio final")
pt = eval(input("Ingresa tu Nota por Tarea: "))
pi = eval(input("Ingresa tu Nota por Interrogacion: "))
ne = eval(input("Ingresa tu Nota por Examen: "))
pp = eval(input("Ingresa tu Nota por Presentacion: "))

promedioFinal =(0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
print(round(promedioFinal,1))
