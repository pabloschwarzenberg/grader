pt = float(input("ingresa la nota de tus tareas: "))
pi = float(input("ingresa la nota de tus interrogaciones: "))
ne = float(input("ingresa la nota de tus examenes: "))
pp = float(input("ingresa la nota de tus presentaciones: "))
pf = (0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp)
pfe = (round(pf,1))
print("tu promedio final de notas es: ", pfe)

