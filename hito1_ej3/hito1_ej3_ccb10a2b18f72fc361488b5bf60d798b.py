S = -123
C = -321
U = -456
R = -789
ingreso = int(input("Ingrese sus ingresos en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("ingrese cuantos hijos tiene: "))
anos = int(input("Ingrese los años de pertenencia en el banco: "))
estado = eval(input("ingrese una S si esta soltero o una C si esta casado: "))
vive = eval(input("Ingrese una U si vive en ciudad o una R si vive en campo: "))
edad = 2020 - nacimiento

if (anos >= 10 and hijos >=2) or (estado == -321 and hijos > 3 and 45 >= edad <=55) or (ingreso == 2500000 and estado ==-123 and vive == -456) or (ingreso == 3500000 and anos >5) or (vive == -789 and estado == -321 and hijos <=1):
    print("APROBADO")
else:
    print("RECHAZADO")


      