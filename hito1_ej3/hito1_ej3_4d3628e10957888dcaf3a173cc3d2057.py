#Aprobación de créditos
Ingreso = eval(input('Ingrese sus ingresos en pesos: '))
AnoNacimiento = eval(input('Ingrese año de nacimiento: '))
NumeroHijos = eval(input('Ingrese numero de hijos: '))
Anos = eval(input('Ingrese años de pertenencia al banco: '))
EstadoCivil = input('Ingrese estado sivil soltero o casado: ')
Ubicacion = input('Ingrese si vive en terreno urbano o rural: ')

Edad =(2020-AnoNacimiento)

soltero ='S'
casado = 'C'

urbano = 'U'
rural = 'R'

if Anos > 10 and NumeroHijos >= 2:
    print('APROBADO')
if EstadoCivil == 'C' and NumeroHijos > 3 and Edad >= 45 and Edad <= 55:
    print('APROBADO')
if Ingreso > 2500000 and EstadoCivil == 'S' and Ubicacion == 'U':
    print('APROBADO')
if Ingreso > 3500000 and Anos > 5:
    print('APROBADO')
if Ubicacion == 'R' and EstadoCivil == 'C' and NumeroHijos < 2:
    print('APROBADO')
    