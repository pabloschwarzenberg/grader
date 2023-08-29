#Aprobación de créditos

ingreso=int(input('ingreso(en pesos):'))
nacimiento=int(input('año de nacimiento:'))
hijos=int(input('cantidad de hijos:'))
banco=int(input('años perteneciendo al banco:'))
estado=str(input('estado civil(S o C):'))
zona=str(input('viven en zona urbana o rural (R o U):'))
años=2020-nacimiento
if (10<=banco)and(2<=hijos):
    print('APROBADO')
else:
    if (estado=='C')and(3<hijos)and(45<=años<=55):
        print('APROBADO')
    else:
        if (ingreso>=2500000)and(estado=='S')and(zona=='U'):
            print('APROBADO')
        else:
            if (ingreso>=3500000)and(banco>=5):
                print('APROBADO')
            else:
                if (zona=='R')and(estado=='C')and(hijos<2):
                    print('APROBADO')
                else:
                    print('RECHAZADO')