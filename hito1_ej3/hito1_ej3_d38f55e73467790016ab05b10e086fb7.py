ingreso = int(input("Ingrese sus ingresos: "))
nacimiento = int(input(" Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el numero de hijos que tiene: "))
años = int(input("Ingrese los años que lleva con nosotros: "))
estado = input("Ingrese su estaco civil con una C si esta casado o S si esta soltero: ")
vive = input("Ingrese si vive en ciudad con U o Campo con R: ")


if (ingreso >= 2500000 and estado == "S" and vive == "U"):
    print("APROBADO")
elif(ingreso >= 3500000 and años >=5):
    print("APROBADO")
elif(estado == "C" and hijos > 3 and nacimiento >= 1966  and nacimiento <= 1976 ):
    print("APROBADO")
elif(años > 10 and hijos >= 2):
    print("APROBADO")
elif(vive == "R" and estado == "C" and hijos < 2):
    print("APROBADO")
     
else:
    print("RECHAZADO")
