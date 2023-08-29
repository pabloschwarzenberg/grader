#Aprobación de créditos
salary = int(input('Ingrese el sueldo: '))
birthdate = int(input('Ingrese el año de nacimiento: '))
birthdate = 2020 - birthdate
num_childs = int(input('Ingrese número de hij@s: '))
years_belonging = int(input('Ingrese años de pertenencia al banco: '))
status = input('Ingrese estado civil, S si es soltero o C si es casado: ')
home = input('Vive en el campo o ciudad, U urbano o R rural: ')

if years_belonging > 10 and num_childs >= 2:
    print('APROBADO')
elif status == 'C' and num_childs > 3 and birthdate >= 45 and birthdate <= 55:
    print('APROBADO')
elif salary > 2500000 and status == 'S' and home == 'U':
    print('APROBADO')
elif salary > 3500000 and years_belonging > 5:
    print('APROBADO')
elif home == 'R' and status == 'C' and num_childs < 2:
    print('APROBADO')
else:
    print('RECHAZADO')