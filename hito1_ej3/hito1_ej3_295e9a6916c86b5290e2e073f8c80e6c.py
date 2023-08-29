#Aprobación de créditos
INGRESO = int(input("Ingrese el ingreso en pesos: "))
ANO_NACIMIENTO = int(input("Ingrese su año de nacimiento: "))
HIJOS = int(input("Ingrese cuantos hjos tiene: "))
ANOS_BANCO = int(input("Años de pertenencia al banco: "))
ESTADO_CIVIL = str(input("Ingrese su estado civil: S si está soltero o C si está casado: "))
VIVIENDA = str(input("Ingrese lugar donde vive: U si vive en lo urbano o R si vive en lo rural: "))
edad = 2020 - ANO_NACIMIENTO
if (ANOS_BANCO>= 10) and (HIJOS>=2):
    print("APROBADO")
elif (ESTADO_CIVIL == "C") and (HIJOS>3) and (45<=edad>=55):
    print("APROBADO")
elif (INGRESO>=2500000) and (ESTADO_CIVIL == "S") and (VIVIENDA == "U"):
    print("APROBADO")
elif (INGRESO>=35000000) and (ANOS_BANCO>=5):
    print("APROBADO")
elif (VIVIENDA == "R") and (ESTADO_CIVIL == "C") and (HIJOS<2):
    print("APROBADO")
else:
    print("RECHAZADO")