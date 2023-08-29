#Nota final
#datos
pt = float(input("nota de tus tareas: "))
pi = float(input("nota de tu interrogaciones: "))
ne = float(input("nota de tu examenes: "))
pp = float(input("nota de tu presentacion: "))
#calculo y resultado
promedio = 0.3*pt + 0.3*pi + 0.3*ne + 0.1*pp

print("tu promedio es: ",(round(promedio,1)))