#Aprobación de créditos

ingreso = input('Ingreso: ')
nacimiento = input('Año de nacimiento: ')
hijos = input('Número de hijos: ')
longitud = input('Años de pertenencia al banco: ')
estado = input('Estado civil: ')
ubicacion = input('Lugar donde habita: ')

if int(longitud) > 10 and int(hijos) >= 2:
    print('APROBADO')
elif estado == 'C' and int(hijos) > 3 and int(nacimiento) > 1962 and int(nacimiento) < 1972:
    print('APROBADO')
elif int(ingreso) > 2500000 and ubicacion == 'U' and estado == 'S':
    print('APROBADO')
elif int(ingreso) > 3500000 and int(longitud) > 5:
    print('APROBADO')
elif ubicacion == 'R' and estado == 'C' and int(hijos) < 2:
    print('APROBADO')
else:
    print('RECHAZADO')
