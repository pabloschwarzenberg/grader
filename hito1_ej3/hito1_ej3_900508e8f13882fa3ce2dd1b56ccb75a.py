ING = int(input('Digite el valor de sus ingresos en pesos: '))
nacimiento = int(input('Ingrese su año de nacimiento: '))
hijos = int(input('Ingrese la cantidad de hijos que usted tiene: '))
APB = eval(input('Ingrese la cantidad de años de pertenencia al banco: '))
EC = input('Indique su estado civil, use una "s" si usted es soltero(a) o una "c" si usted es casado(a): ')
vive = input('Indique usando "u" si vive en ciudad o usando "r" si vive en zona rural (campo): ')

edad = 2020-nacimiento
s = 1
c = 2

u = 3
r = 4

if (APB > 10) and (hijos >= 2):
    print('APROBADO.')
else:
    print('RECHAZADO.')

if (EC == 2) and (hijos > 3) and (edad >= 45) or (edad <= 55):
    print('APROBADO.')
else:
    print('RECHAZADO.')

if (ING > 2500000) and (EC == 1) and (vive == 3):
    print('APROBADO.')
else:
    print('RECHAZADO.')

if (ING > 3500000) and (APB > 5):
    print('APROBADO.')
else:
    print('RECHAZADO.')

if (vive == 4) and (EC == 2) and (hijos > 2):
    print('APROBADO.')
else:
    print('RECHAZADO.')

