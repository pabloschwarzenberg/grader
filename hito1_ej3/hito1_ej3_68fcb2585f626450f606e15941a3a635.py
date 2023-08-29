ingreso=eval(input("introduzca el ingreso"))
anonacimiento=eval(input("ingrese año nacimiento"))
numh=eval(input("ingrese numero de hijos"))
anoenbanco=eval(input("años en banco"))
escivil=str(input("soltero S o casado C"))
vive=str(input("urbano U o rural R"))
edad=anonacimiento-2020

if 10<=anoenbanco and numh>=2:
    print("APROBADO")
else:
    if escivil=="C" and numh>=3 and 45<=edad>=55:
       print("APROBADO")
    else:
        if ingreso>=2500000 and escivil=="S" and vive=="U":
            print("APROBADO")
        else:
            if ingreso>=3500000 and anoenbanco>=5:
                print("APROBADO")
            else:
                if vive=="R" and escivil=="C" and numh<=2:
                      print("APROBADO")
                else:
                     print("RECHAZADO")
