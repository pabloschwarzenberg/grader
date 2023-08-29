ingreso  =int(input("Ingreso mensual: "))
año      =int(input("Año de nacimiento: "))
hijos    =int(input("Numero de hijos: "))
añosbanco=int(input("Años de permanencia en banco: "))
estado   =input("Estado civil: ")
# C:casado, # S: soltero
vive     =input("Donde vive: ")
# U: urbano, # R: rural
c=estado
s=estado
u=vive
r=vive
edad=(2021-año)

if añosbanco > 10 and hijos >=2:
    print("APROBADO")
elif añosbanco <= 10 and hijos <2:
    print("RECHAZADO")
elif estado == c and hijos >3 and edad >45 and edad<55:
    print("APROBADO")
elif estado == s and hijos <3 and edad <45 and edad>55:
    print("RECHAZADO")
elif ingreso >2500000 and estado == s and vive == u:
    print("APROBADO")
#elif ingreso <2500000 and estado == c and vive == r:
#    print("RECHAZADO")
elif ingreso >3500000 and añosbanco > 5:
    print("APROBADO")
elif ingreso <3500000 and añosbanco < 5:
    print("RECHAZADO")
elif vive ==r and estado == c and hijos < 2:
    print("APROBADO")
elif vive ==u and estado == s and hijos >= 2:
    print("RECHAZADO")