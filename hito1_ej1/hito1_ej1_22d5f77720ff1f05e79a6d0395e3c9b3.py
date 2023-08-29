#Nota final
pt = float(input("Ingrese su nota de tareas: "))
pi = float(input("Ingrese su nota de interrogacion: "))
ne = float(input("Ingrese su nota de examen: "))
pp = float(input("Ingrese su nota de presentacion: "))

calculo = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

redondeo = round(calculo,1)

print("Su promedio final es: ",redondeo)
