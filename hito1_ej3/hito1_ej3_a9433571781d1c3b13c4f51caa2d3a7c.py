ingreso = int(input("Ingrese su ingreso: "))
año = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
años_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado = input("Ingrese su estado civil: ")
vive = input("Ingrese donde reside: ")

if años_banco > 10 and hijos >= 2:
    print("APROBADO")

elif estado == 'C' and hijos > 3 and 1967 < año > 1977:
    print("APROBADO")

elif ingreso > 2500000 and estado == 'S' and vive == 'U':
    print("APROBADO")

elif ingreso > 3500000 and años_banco > 5:
    print("APROBADO")

elif vive == 'R' and estado == 'C' and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")