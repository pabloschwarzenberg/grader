#Nota final
pt = eval(input("Ingrese su nota de tareas: "))
pi = eval(input("Ingrese su nota de interrogaciones: "))
ne = eval(input("Ingrese su nota de examen: "))
pp = eval(input("Ingrese su nota de presentacion: "))

promedio = (pt*0.3) + (pi*0.3) + (ne*0.3) + (pp*0.1)
redondeo = round(promedio, 1)
print(redondeo)
