#Entradas
ingreso = int(input("ingrese los ingresos: "))
nacimiento = int(input("ingrese año de nacimiento: "))
hijos = int(input("ingrese numero de hijos: "))
pertenencia = int(input("ingrese anos de pertenencia al banco: "))
estado= str(input("ingrese S si es soltero, o C si es casado: "))
vive= str(input("ingrese U si vive en el campo, o R si vive en ciudad: "))
S=1
C=2
U=3
R=4
if (( 10 > pertenencia) and ( 2 >= hijos)):
    print("APROBADO")
elif ((estado == 2) and (3 > hijos) and (1976 < nacimiento < 1966)):
    print("APROBADO")
elif ((2500000 > ingreso) and (estado == 1) and (vive == 4)):
    print("APROBADO")
elif ((3500000 > ingreso) and (5 < pertenencia)):
    print("APROBADO")
elif ((vive == 3) and (estado == 2) and (2 < hijos)):
    print("APROBADO")
else:
    print("RECHAZADO")