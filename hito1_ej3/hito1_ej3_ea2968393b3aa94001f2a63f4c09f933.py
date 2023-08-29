#Aprobación de créditos
Ingreso=int(input('Digite su ingreso porfavor'))
Añodenacimiento=int(input('Ingrese su año de nacimiento'))
Numerodehijos=int(input('Ingrese su cantidad de hijos'))
Añosdepertenencia=int(input('Ingrese su años de pertenencia en el banco'))
Estadocivil=input('Ingrese una S si esta soltero o ingrese una C si esta casado')
Vivienda=input('Ingrese una U si vive en ciudad o ingrese una R si vive en campo')

Edad=2020-Añodenacimiento

if Añosdepertenencia >10 and Numerodehijos>=2:
    print('APROBADO')


elif Estadocivil=='C' and Numerodehijos>3 and 55<=Edad>=45:
    print('APROBADO')


elif Ingreso>=2500000 and Estadocivil=='S' and Vivienda=='U':
    print('APROBADO')


elif Ingreso>=3500000 and Añosdepertenencia>5:
    print('APROBADO')
    

elif Vivienda=='R' and Estadocivil=='C' and Numerodehijos<2:
    print('APROBADO')


else:   print('RECHAZADO')  