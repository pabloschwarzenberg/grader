#Nota final
pt=float(input("Ingrese su nota de tareas: "))
pi=float(input("Ingrese su nota de Interrogaciones:"))
ne=float(input("Ingrese su nota de Examenes: "))
pp=float(input("Ingrese su nota de Presentaciones: "))
calculo = (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
print(round(calculo,1))      