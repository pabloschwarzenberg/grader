# Sistema de Ecuaciones
# ax + by = c
# dx + ey = f

a = int(input("Ingrese el número para a: "))
b = int(input("Ingrese el número para b: "))
c = int(input("Ingrese el número para c: "))
d = int(input("Ingrese el número para d: "))
e = int(input("Ingrese el número para e: "))
f = int(input("Ingrese el número para f: "))

determinante = a*e - b*d

if determinante != 0:
    x =(c*e - b*f) / determinante
    y =(a*f - c*d) / determinante
    print("x=" +str(x) + "y=" +str(y))

else:
    print("Incorrecto, esta ecuación no tiene solución, intenta con otro")      