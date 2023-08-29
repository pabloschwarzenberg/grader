#Aprobación de créditos
ANIO_ACTUAL= 2020
ANIO= 0
ESTADO= " "
INGRESOS= int(input("Registre ingreso (en peso):"))
ANIO_NAC= int(input("ingrese anio de naciomiento:"))
N_HIJOS= int(input("ingrese cantidad de hijos:"))
ANIO_PERTENENCIA= int(input("ingrese anios de pertencia al banco:"))
ESTADO_CIVIL= str(input("ingrese estado civil (soltero, casado):"))
LUGAR_DE_RESIDENCIA= input("ingrese lugar donde vive (Urbano,Rural):")
if ANIO_PERTENENCIA >= 10 and N_HIJOS >= 2:
    print("APROBADO")
elif ESTADO_CIVIL == "C" and 45 <= (ANIO_ACTUAL- ANIO_NAC) <= 55:
    print("APROBADO")
elif INGRESOS >= 2500000 and ESTADO_CIVIL == "S" and LUGAR_DE_RESIDENCIA == "U":
    print("APROBADO")
elif INGRESOS >= 3500000 and ANIO_PERTENENCIA == 5:
    print("APROBADO")
elif LUGAR_DE_RESIDENCIA == "R" and ESTADO_CIVIL == "S" and N_HIJOS < 2:
     print("APROBADO")
else:
     print("RECHAZADO")  