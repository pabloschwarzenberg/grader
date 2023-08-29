#Aprobación de créditos
ingreso = int(input('ingrese su ingreso (en pesos): '))
nacimiento = int(input('ingrese su año de nacimiento: '))
nhijos = int(input('ingrese el numero de hijos que tiene: '))
abanco = int(input('ingrese los años de pertenencia al banco: '))
estado = input('ingrese su estado (soltero(S) o casado(C): ')
viven = input('ingrese su vivienda(campo(R) o ciudad(U): ')

pro = (2021 - nacimiento)
if abanco == 10 and nhijos >=2:
    print('Aprobado')
if str(estado.upper())== 'C' and nhijos > 3 and pro >= 45 and pro <= 55:
    print('Aprobado')
if ingreso > int(2500000) and str(estado.upper()) == 'S' and str(viven()) == 'U':
    print('Aprobado')
if str(viven.upper()) == 'R' and str(estado.upper()) == 'C' and nhijos < 2:
    print('Aprobado')
if ingreso > int(3500000) and abanco > 5:
    print('Aprobado')
      