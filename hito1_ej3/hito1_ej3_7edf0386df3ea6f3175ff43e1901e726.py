#Aprobación de créditos
IEP = int(input("Ingreso en pesos: "))
ADN = int(input("Año de nacimiento: "))
NDH = int(input("Numero de hijos: "))
ADPAB = int(input("Año de pertenencia al banco: "))
ECC = input("S:soltero, C:casado: ")
COC = input("U:urbano, R:rural: ")

EDAD = (2021 - ADN)

if ADPAB > 10 and NDH >= 2:
    print("APROBADO")

elif ECC == "C" and (NDH > 3) and(EDAD >= 45) and (EDAD <= 55):
    print("APROBADO")

elif IEP >= 2500000 and ECC == "S" and COC  == "U":
    print("APROBADO")

elif IEP == 3500000 and ADPAB > 5:
    print("APROBADO")

elif COC == "R" and ECC == "C" and NDH < 2:
    print("APROBADO")

else:
    print("RECHAZADO")     