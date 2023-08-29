#Aprobación de créditos
salary = int(input('Ingrese el sueldo: '))
cumpleanos = int(input('Ingrese el año de nacimiento: '))
cumpleanos='2003'
num_ninos = int(input('Ingrese número de hij@s: '))
anos_bank = int(input('Ingrese años de pertenencia al banco: '))
sp = input('estado civil, S si es soltero o ;C si es casado:')
lugar =input('Vive en el campo o ciudad, U urbano o R rural: ')
if anos_bank > 10 and num_ninos >= 2:
    print('APROBADO')
elif sp == 'C' and num_ninos > 3 and cumpleanos>= 45 and cumpleaños <= 55:
    print=('APROBADO')
elif salary > 2500000 and sp== 'S' and home == 'U':
    print('APROBADO')
elif salary > 3500000 and anos_bank > 5:
    print('APROBADO')
elif lugar == 'R' and sp== 'C' and num_ninos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')