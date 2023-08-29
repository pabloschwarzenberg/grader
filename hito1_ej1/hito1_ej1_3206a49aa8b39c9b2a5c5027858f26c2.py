#Nota final
pt = float(input("Ingrese Nota Tareas: "))
pi = float(input("ingrese Nota Interrogaciones: "))
ne = float(input("ingrese Nota Examen: "))
pp = float(input("ingrese Nota Presentacion: "))
resultado = round((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp), 1)
print(str(resultado))