#Aprobación de créditos
ingreso=int(input('Ingresos:'))
añodenacimiento=int(input('Fecha de nacimiento:'))
hijos=int(input('Numero de hijos:'))
añosdebanco=int(input('Años de pertenencia al banco:'))
estadocivil=input('Estado civil:')
hogar=input('Si vivie en campo o ciudad:')


años=añodenacimiento%10000
edad=2020-años


if añosdebanco>10 and hijos>=2:
    print('APROBADO')
if estadocivil=='C' and hijos>3 and 45>edad>55:
    print('APROBADO')
if ingreso>2500000 and estadocivil=='S' and hogar=='U':
    print('APROBADO')
if ingreso>3500000 and añosdebanco>5:
    print('APROBADO')
if hogar=='R' and estadocivil=='C' and hijos<2:
    print('APROBADO')
else:
    print('RECHAZADO')          