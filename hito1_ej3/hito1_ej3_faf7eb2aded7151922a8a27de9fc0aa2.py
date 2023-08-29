#Aprobación de créditos
ING = int(input('Ingresar ingresos en pesos: '))
ADN = int(input('Ingresar año de nacimiento: '))
NDH = int(input('Ingresar número de hijos: '))
ADPB = eval(input('Ingresar años de pertenencia al banco: '))
EC = input('Ingresar su estado civil, en el caso de que sea soltero(a) indiquelo con una "S" y en el caso de ser casado indique con una "C": ')
SVCC = input('Indique si vive en campo o ciudad, en el caso de ser de ciudad indique con una "U" y en el caso de ser de campo indiquelo con una "R": ')

edad = 2020-ADN
S = 1
C = 2

U = 3
R = 4

if (ADPB > 10) and (NDH >= 2):
    print('APROBADO.')
else:
    print('RECHAZADO.')

if (EC == 2) and (NDH > 3) and (edad >= 45) or (edad <= 55):
    print('APROBADO.')
else:
    print('RECHAZADO.')

if (ING > 2500000) and (EC == 1) and (SVCC == 3):
    print('APROBADO.')
else:
    print('RECHAZADO.')

if (ING > 3500000) and (ADPB > 5):
    print('APROBADO.')
else:
    print('RECHAZADO.')

if (SVCC == 4) and (EC == 2) and (NDH > 2):
    print('APROBADO.')
else:
    print('RECHAZADO.')
     