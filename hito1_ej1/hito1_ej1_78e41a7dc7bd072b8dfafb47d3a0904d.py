#Nota final
#Para el ingreso de notas se considera notas con 1 decimal (ej: 4.8)
#Ingreso de datos
pt = float(input("Ingrese su nota de tareas: "))
pi = float(input("Ingrese su nota de interrogaciones: "))
ne = float(input("Ingrese su nota de examen: "))
pp = float(input("Ingrese su nota de presentación: "))

#Calculo
nota_final=(0.3*pt+0.3*pi+0.3*ne+0.1*pp)
redondeo=round(nota_final, 1)
print("Su nota final es:", redondeo)