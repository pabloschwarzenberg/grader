#Aprobación de créditos
numhijos= int(input("ingrese cantidad de hijos:"))
aEnbanco= int(input("cantidad de años que pertenece al banco:"))
estCivil= input("soltero 'S' o casado 'C':")
while not(estCivil=='C' or estCivil=='S'):
    estCivil= input(" error soltero'S' o casado 'C':")
vive= input("localidad rural 'R' o urbana 'U':")
while not( vive=='R' or vive=='U'):
    vive= input(" error localidad rural 'R' o urbana 'U':")
edad= anActual - aNac

if(aEnbanco>10 and numhijos>=2):
    print("APROBADO:")
elif(estCivil=="C" and numhijos>3 and edad>=45 and edad<=55):
    print("APROBADO:")
elif(ingreso>2500000 and estCivil=="S" and vive=="U"):
    print("APROBADO:")
elif(ingreso>3500000 and aEnbanco>=5):
    print("APROBADO:")
elif(vive=="R" and estCivil=="C" and numhijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")
          