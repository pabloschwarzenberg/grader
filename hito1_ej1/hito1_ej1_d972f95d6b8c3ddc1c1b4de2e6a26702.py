#Nota final

pt = eval(input("Favor de ingresar nota de tareas: "))
pi = eval(input("Favor de ingresar nota por interrogaciones: "))
ne = eval(input("Favor de ingresar nota de examen: "))
pp = eval(input("Favor de ingresar nota de presentación: "))

calculo = (0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)

resultado = round(calculo,1)

print("el promedio final es de: ",resultado)

