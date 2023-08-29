#Aprobación de créditos
C=1
S=2
U=3
R=4

ingreso =eval(input('Ingreso (en pesos):'))
añonacimiento=eval(input('Año de nacimiento:'))
numerohijos=eval(input('Número de hijos:'))
añobanco=eval(input('Año de pertenencia al banco:'))
estadocivil=eval(input('Estado civil (S: soltero- C: casado:):'))
campociudad=eval(input('Si vive en campo o cuidad(U: urbano, R: rural): '))

if añobanco>=10 and numerohijos>=2:
    print(' APROBADO')
elif numerohijos>3 and  1965 <=añonacimiento<=1975 and estadocivil==1:
    print(' APROBADO')
elif ingreso>2500000 and estadocivil==2 and campociudad==3:
    print(' APROBADO')
elif ingreso>3500000 and añobanco >5:
    print(' APROBADO')
elif estadocivil==1 and numerohijos<2:
    print(' APROBADO')
else:
    print('RECHAZADO')
        


   



      