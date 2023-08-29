#Aprobación de créditos
ingreso = int(input("Inserte su ingreso: "))
año = int(input("Ingrese su año de nacimiento: "))
numHijos = int(input("Ingrese el numero de hijos: "))
añosPert = int(input("Ingrese sus años de pertenencia al banco: "))
estCivil = str(input("Inserte su estado civil, casado o soltero (C o S): "))
dondeVive = str(input("Inserte su lugar de procedencia, campo o cuidad (R o C): "))
if añosPert >= 10 and numHijos >= 2 or estCivil == "C" and numHijos > 3 and año >= 1968 and año <= 1976 or ingreso > 2500000 and estCivil == "S" and dondeVive == "C" or ingreso > 3500000 and añosPert > 5 or dondeVive == "R" and estCivil == "C" and numHijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      