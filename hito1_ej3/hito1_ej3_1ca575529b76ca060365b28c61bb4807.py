ingresos = int(input('ingrese la cantidad de ingresos mensuales:'))
nacimiento = int(input('Ingrese su año de nacimiento:'))
nhijos = int(input('Ingrese numero de hijos:'))
years = int(input('Ingrese sus años de pertenencia al banco:'))
estadocivil = str(input('Ingrese su estado civil (S: soltero / C: Casado):'))
cc = str(input('¿Usted pertenece a la zona urbana(U) o rural(R)?'))
aos = 2021 - nacimiento

if years > 10 and nhijos >= 2:
    print('APROBADO')
elif estadocivil == str('c') and nhijos > 3 and aos > 45 and aos < 55:
    print('APROBADO')
elif ingresos > 2500000 and estadocivil == str('S') and nhijos < 2:
    print('APROBADO')
elif ingresos > 3500000 and years > 5:
    print('APROBADO')
elif cc == str('R') and estadocivil == str('C') and nhijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')     