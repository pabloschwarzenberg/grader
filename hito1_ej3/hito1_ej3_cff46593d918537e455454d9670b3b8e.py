#Aprobación de créditos
ingreso=int(input("ingreso en pesos: "))
ano_nacimiento=int(input("año de nacimiento: "))
hijos=int(input("numero de hijos: "))
anos_pertenencia=int(input("años de pertenencia al banco: "))
estado=str(input("estado civil S o C: "))
zona=str(input("vive en zona urbana o rural U o R: "))
edad=int(2017-ano_nacimiento)
C=0
S=1
U=0
R=1
if anos_pertenencia>10 and hijos>=2:
    print("APROBADO")
else:
    if estado=='C' and hijos>3 and 45<edad<55:
        print("APROBADO")
    else:
        if ingreso>2500000 and estado=='S' and zona=='U':
            print("APROBADO")
        else:
            if ingreso>3500000 and anos_pertenencia>5:
                print("APROBADO")
            else:
                if zona=='R' and estado=='C' and hijos<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")

