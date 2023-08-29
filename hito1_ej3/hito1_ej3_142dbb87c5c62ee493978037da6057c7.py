#Aprobación de créditos
ingresos = eval(input('ingresos cliente en pesos: '))
añodenacimiento = eval(input('año de nacimiento cliente:'))
numerodehijos = eval(input('numero de hijos del cliente:'))
añosdepertenenciaalbanco = eval(input('años de pertenencia al banco:'))
estadocivil = input('soltero o casado:')
campoociudad = input('urbano o rural:')

s = estadocivil = 1
c = estadocivil = 2
u = campoociudad = 3
r = campoociudad = 4
edad = 2019-añodenacimiento
if añosdepertenenciaalbanco >= 10 and numerodehijos >= 2 or 'c'  and numerodehijos > 3 and 45 <= edad <= 55 or ingresos > 2500000 and 's' and 'u' or ingresos > 3500000 and añosdepertenenciaalbanco > 5 or 'r' and 'c' and numerodehijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')
          