import datetime
currentDateTime = datetime.datetime.now()
ingreso=0
nacimiento=0
hijos=0
tiempo=0

ingreso=int(input("Registre su Ingreso en pesos:"))
nacimiento=int(input("Registre año de naciminto:"))
hijos=int(input("Registre cantidad de hijos:"))
tiempo=int(input("Registre cantidad de antiguedad en banco:"))
estcivil=input("Registre estado civil S:Soltero o C:Casado :")
tipo=input("Registre tipo de lugar U:Urbano o R:Rural :")

date=currentDateTime.date()
edad=(date.year)-nacimiento


if (tiempo>10) and (hijos>=2):
    print("CREDITO APROBADO")
elif (estcivil=='C') and (hijos>3) and (edad>=45 and edad<=55):
    print("CREDITO APROBADO")
elif (estcivil=='S') and (ingreso>2500000) and (tipo=='U'):
    print("CREDITO APROBADO")
elif (ingreso>3500000) and (tiempo>5):
    print("CREDITO APROBADO")
elif (estcivil=='C') and (hijos<2) and (tipo=='R'):
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")
