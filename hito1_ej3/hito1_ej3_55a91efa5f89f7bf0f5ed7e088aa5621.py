#Aprobación de créditos
print("\n==========================================\nBienvenido a el sistema automatico de aprobación de credito\n==========================================\nPorfavor ingrese los siguientes datos")
ingreso = int(input("Su ingreso en pesos: "))
ano = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el numero de hijos que tiene: "))
anobanco = int(input("Ingrese los años de pertenencia que lleva en el banco: "))
estadocivil = input("ingrese su estado civil con las siglas, S si usted esta soltero y, C si esta casado: ")
vive = input("Ingrese su vivienda con las siglas, U si es urbano y, R si es rural: ")

anoactual= 2020
edad = (anoactual - ano)

if anobanco >= 10 and hijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
if estadocivil == "C" and hijos >= 3 and (edad >= 45 or edad <= 55):
    print("APROBADO")
else:
    print("RECHAZADO")
if ingreso >= 2500000 and estadocivil == "S" and vive == "U":
    print("APROBADO")
else:
    print("RECHAZADO")
if ingreso >= 3500000 and anobanco >= 5:
    print("APROBADO")
else:
    print("RECHAZADO")
if vive == "R" and estadocivil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      