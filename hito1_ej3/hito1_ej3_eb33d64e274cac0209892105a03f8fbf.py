#Aprobacion de creditos
import datetime
ingreso=int(input("Digita tu ingreso en pesos: "))
anActual= datetime.datetime.now().year
aNac= int(input("Digita tu año de nacimiento: "))
while not (aNac>=1900 and aNac<=anActual):
    aNac= input("Error...Digita nuevamente tu año nacimiento: ")
numhijos= int(input("Digita cantidad de hijos: "))
añosenbanco= int(input("¿Hace cuantos años pertenece al banco?: "))
estado_civil= input("¿Soltero (S) o Casado (C)?: ")
while not (estado_civil=="C" or estado_civil=="S"):
    estado_civil=input("Error...¿Soltero (S) o Casado(C)?: ")
residencia=input("¿Vive en una localidad rural(R) o Urbana(U)?: ")
while not (residencia=="R" or residencia=="U"):
    residencia=input("Error...¿Vive en una localidad rural(R) o Urbana(U)?: ")
edad=anActual - aNac
if(añosenbanco>10 and numhijos>=2):
    print("APROBADO")
elif (estado_civil=="C" and numhijos>3 and edad>=45 and edad<=55):
    print("APROBADO")
elif(ingreso>2500000 and estado_civil=="S" and residencia=="U"):
    print("APROBADO")
elif(ingreso>3500000 and añosenbanco>=5):
    print("APROBADO")
elif(residencia=="R" and estado_civil=="C" and numhijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")