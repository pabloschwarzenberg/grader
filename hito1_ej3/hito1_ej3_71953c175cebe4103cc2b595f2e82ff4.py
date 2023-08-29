#Aprobación de créditos
import datetime
ingreso = int(input ("¿Ingresos en pesos?: "))
anActual = datetime.datetime.now().year #rescata año actual
aNac= int(input ("¿Año de nacimiento?: "))
while not(aNac>=1900 and aNac<=anActual):
   aNac = input("Error....¿Año de nacimiento?:  ")
numhijos = int(input ("¿Cantidad de hijos?: "))
aEnbanco = int(input ("¿Años de pertenencia en banco?: "))
estCivil = input ("¿Soltero (S) o Casado (C)?: ")
while not(estCivil=="C" or estCivil=="S"):
   estCivil = input("Error....¿Soltero (S) o Casado (C)?: ")
vive = input("¿Vive en localidad rural (R) o Urbana(U): ")
while not(vive=="R" or vive=="U"):
   vive = input("Error.. ¿Vive en localidad rural (R) o Urbana(U)?: ")
edad = anActual - aNac
if (aEnbanco>10 and numhijos>=2):
    print("APROBADO")
elif (estCivil=="C" and numhijos>3 and edad>=45 and edad<=55):
    print("APROBADO")
elif (ingreso>2500000 and estCivil=="S" and vive=="U"):
    print("APROBADO")
elif (ingreso>3500000 and aEnbanco>=5):
    print("APROBADO")
elif (vive=="R" and estCivil=="C" and numhijos<2):
    print("APROBADO")  
else:
    print("RECHAZADO")