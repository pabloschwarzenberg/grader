#Aprobación de créditos
ingreso    =int(input('registra tus ingresos:'))
años_edad  =int(input('registra tu año de nacimiento:'))
hijos      =int(input('registra la cantidad de hijos que tengas:'))
años_banco =int(input('registra la cantidad de años que llevas con nosotros:'))
civil      =str(input('registra tu estado civil("S" soltero, "C" casado):'))
Cam_ciu    =str(input('registra si eres de zona urbana o rural("U" urbano, "R" rural):'))
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
while ingreso!=0:
    if (ingreso>2500000 and Cam_ciu=='R') or (ingreso>3500000 and años_banco>5) or (Cam_ciu=='U' and hijos<2) or (civil=='C' and 1967<=años_edad<=1977) or (años_banco>10 and 2<=hijos):
        print ('APROBADO')
    else:
        print('RECHAZADO')
    break
