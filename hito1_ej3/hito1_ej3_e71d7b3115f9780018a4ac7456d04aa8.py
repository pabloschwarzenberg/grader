#Aprobación de créditos
ingresos = float(input("Ingresar sus ingresos:  $"))
anonacim = float(input("Ingrese su año de nacimiento: "))
numhij = float(input("Ingese el número de hijos: "))
anoperma = float(input("Ingrese el año de permanencia: "))
estadocivil = str(input("Ingrese su estado civil: "))
vive = str(input("Ingrese donde vive: "))

if anoperma >=10 and numhij >=2 and anonacim >= 1966 and anonacim <= 1975:
    print("APROBADO")
elif estadocivil == "C" and numhij >=3:
    print("APROBADO")
elif ingresos > 2500000 and estadocivil == "S" and vive == "U":
    print("APROBADO")
elif ingresos > 3500000 and anoperma > 5:
    print("APROBADO")
elif vive == "R" and estadocivil == "C" and numhij <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
