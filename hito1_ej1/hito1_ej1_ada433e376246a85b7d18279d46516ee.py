#Nota final
pt = float(input("Ingrese Nota de Tarea: "))
pi = float(input("Ingrese Nota de Interrogaciones: "))
ne = float(input("Ingrese Nota de Examen: "))
pp = float(input("Ingrese Nota de Presentacion: "))
 
pt1 = 0.3*pt
pi2 = 0.3*pi
ne3 = 0.3*ne
pp4 = 0.1*pp
 
promedio = (pt1 + pi2 + ne3 + pp4)
 
print(round(promedio,1))