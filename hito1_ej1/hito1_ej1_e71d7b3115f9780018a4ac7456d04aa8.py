#Nota final
pt = eval(input("Ingrese la nota de las tareas: "))
pi = eval(input("Ingrese la nota de las interrogaciones: "))
ne = eval(input("Ingrese la nota del examen: "))
pp = eval(input("Ingrese la nota de la presentación: "))

promedio = 0.3 *pt+ 0.3*pi+0.3*ne+0.1*pp
redondeo = round(promedio,1)

print("La nota promedio es ",redondeo)   