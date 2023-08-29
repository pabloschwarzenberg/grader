#Aprobación de créditos
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
anosbanco=int(input())
estadocivil=input()
vivienda=input()
if anosbanco>10:
    print("APROBADO")
else:
    if estadocivil==C and hijos>3 and 55>nacimiento-2018>45:
        print("APROBADO")
    else:
        if ingreso>2500000 and estadocivil==S and vivienda==U:
            print("APROBADO")
        else:
            if ingreso>35000000 and anosbanco>5:
                print("APROBADO")
            else:
                if vivienda==R and estadocivil==C and hijos<2:
                    print("APROBADO")
                else:
                    print("REPROBADO")      