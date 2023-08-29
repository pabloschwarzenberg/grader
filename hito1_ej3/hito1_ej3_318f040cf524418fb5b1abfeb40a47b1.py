#Aprobación de créditos
ingreso = int(input())
anoNacimiento = int(input())
numHijos = int(input())
anosBanco = int(input())
estadoCivil = input()
uOr = input()
edad = anoNacimiento - 2023

if anosBanco > 10 and numHijos >= 2:
    print("APROBADO")
elif estadoCivil.upper() == "C" and numHijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estadoCivil.upper() == "S" and uOr.upper() == "U":
    print("APROBADO")
elif ingreso > 3500000 and anosBanco > 5:
    print("APROBADO")
elif uOr.upper() == "R" and estadoCivil.upper() == "C" and numHijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")