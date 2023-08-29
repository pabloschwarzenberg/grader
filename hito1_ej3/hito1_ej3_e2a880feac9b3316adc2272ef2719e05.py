#Aprobación de créditos
import datetime
ingreso = int(input("ingresos ingreso en pesos: "))
#aActual = int(input("ingrese año actual: "))
aActual = datetime.datetime.now().year #rescata año actual
aNacimiento = int(input("año nacimiento: "))
while not (aNacimiento>=1900 and aNacimiento <= aActual):
    aNacimiento = int(input("error .... año de nacimiento?: "))
numhijos = int(input("cantidad de hijos: "))
aEnbanco = int(input("antiguedad en el banco: "))

estadocivil = input("soltero(S) o casado (C): ")
while not(estadocivil == "S" or estadocivil == "C"):
    estadocivil = input("soltero(S) o Casado (C): ")
    
    
vive = input("vive en localidad rural (R) o urbana (U): ")
while not (vive == "R" or vive == "U"):
          vive = input("vive en localidad rural (R) o urbana (U): ")
edad = aActual - aNacimiento
if (aEnbanco>10 and numhijos>=2):
    print ("APROBADO")
elif (ingreso>2500000 and estadocivil == "S" and vive == "U"):
    print("APROBADO")
elif (ingreso>3500000 and aEnbanco>=5):
    print("APROBADO")
elif (vive=="R" and estadocivil == "C" and numhijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")