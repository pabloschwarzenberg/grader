#Aprobación de créditos
ingreso=int(input("introduzca el ingreso :"))
anonacimiento=int(input("ingrese año nacimiento :"))
numh=int(input("ingrese numero de hijos :"))
anoenbanco=int(input("años en banco : "))
estadocivil=input("soltero S o casado C :")
vive=input("urbano U o rural R : ")
edad=2020-anonacimiento

if anoenbanco>10 and numh>=2:
    print("APROBADO")
else:
    if estadocivil=="C" and numh>3 and (edad>=45 or edad<=55):
        print("APROBADO")
    else:
        if ingreso>2500000 and estadocivil=="S" and vive=="U":
               print("APROBADO")
        else:
            if ingreso>3500000 and anoenbanco>5:
               print("APROBADO")
            else:
                if vive=="R" and estadocivil=="C" and numh<2:
                   print("APROBADO")
                else:
                    print("RECHAZADO")