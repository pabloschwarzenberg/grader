#Aprobación de créditos
S = 1
C = 2
U = 3
R = 4
ingreso = eval(input('ingresa tu ingreso en pesos: '))
ano = eval(input('ingrese su año de nacimiento: '))
hijo = eval(input('ingrese cantidad de hijos: '))
anosbanco = eval(input('ingrese años de pertenenia al banco: '))
print('1 = soltero')
print('2 = casado')
estadocivil = eval(input('ingrese Estado civil: '))
print('3 = urbano')
print('4 = rural')
ciudad = eval(input('usted vive en: '))

edad = 2020 - ano

if 10 < anosbanco:
    if 2 <= hijo:
        print('APROBADO')

if estadocivil == C:
    if  3 <= hijo:
        if 45 <= edad <=55:
            print('APROBADO')

if ingreso > 2500000:
    if estadocivil == S:
        if ciudad == U:
            print('APROBADO')

if ingreso > 3500000:
    if anosbanco > 5:
        print('APROBADO')

if ciudad == 4:
    if estadocivil == 2:
        if 2 > hijo:
            print('APROBADO')
else:
    print('RECHAZADO')       