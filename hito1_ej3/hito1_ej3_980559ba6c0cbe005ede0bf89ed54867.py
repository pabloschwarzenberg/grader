#Aprobación de créditos
ingr = int(input('Ingreso (en pesos) = '))
an   = int(input('Año de nacimiento = '))
nh   = int(input('Numero de hijos = '))
apb  = int(input('Años de pertenencia al banco = '))
ec   = str(input('Estado civil ("S": soltero, "C", casado) = '))
coc  = str(input('Vive en campo o cuidad ("U": urbano, "R": rural) = '))

if apb > 10 and nh >= 2:
    print('APROBADO')

elif ec == 'C' and nh > 3 and an >= 45 and an <= 55:
    print('APROBADO')

elif ingr > 2500000 and ec == 'S' and coc == 'U':
    print('APROBADO')

elif ingr > 3500000 and apb > 5:
    print('APROBADO')

elif coc == 'R' and ec == 'C' and nh < 2:
    print('APROBADO')

else:
    print('RECHAZADO')
      