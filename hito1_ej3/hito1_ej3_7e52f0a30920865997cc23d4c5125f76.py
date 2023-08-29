#Aprobación de créditos
ingresos=int(input("Ingrese el valor de sus ingresos: "))
nacimiento=int(input("Ingrese el año de nacimiento de usted: "))
años=2020-(nacimiento)
hijos=int(input("Cantidad de hijos que usted tiene: "))
añobanco=int(input("Cantidad de años que lleva de pertenencia en nuestro banco: "))
estadocivil=input("Su Estado civil Si es Soltero escriba la letra'S' o  Si es  Casado escriba la letra'C' :")
S= estadocivil
C= estadocivil
vive=input("Zona donde usted vive, Si usted vive en una Zona Urbana escriba la letra 'U' o Si vive en una Zona Rural escriba la letra 'R'")
if(añobanco>10 and hijos>=2):
    print("APROBADO")
elif(estadocivil==S and 45<=años<=55):
    print("APROBADO")
elif(ingreso>2500000 and estadocivil==S and vive==U):
    print("APROBADO")
elif(ingreso>3500000 and añobanco>5):
    print("APROBADO")
elif(vive==2 and estadocivil==C and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")       