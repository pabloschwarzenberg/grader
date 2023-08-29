#Aprobación de créditos
ingreso = int(input("Ingrese sus ingresos:"))
cumple = int(input("Ingrese su año de nacimiento:"))
hijos = int(input("Ingrese el número de hijos que tenga:"))
años_banco = int(input("Ingrese sus años de pretenencia al banco:"))
ecivil = str(input("Ingrese su estado civil (S:soltero, C:casado):"))
lugar = str(input("Ingrese si vive en campo o ciudad(U:urbano, R:rural):"))
if años_banco > 10 and hijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")

if ecivil == str("C") and hijos > 3 and 1963 < cumple < 1973:
    print("APROBADO")
else:
    print("RECHAZADO")

if ingreso > 2500000 and ecivil == str("S") and lugar == str("U"):
    print("APROBADO")
else:
    print("RECHAZADO")

if ingreso > 3500000 and años_banco > 5:
    print("APROBADO")
else:
    print("RECHAZADO")

if lugar == str("R") and ecivil == str("C") and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")