#Aprobación de créditos
Ingreso=eval(input('Ingresos :'))
Año=eval(input('Fecha de Nacimiento: '))
hijos=eval(input('Hijos: '))
Añosconbanco=eval(input('Años con el banco:'))
Estadocivil=input('S o C:')
Residencia=input('U o R:')

if ((Añosconbanco>10 and hijos>=2) or (Estadocivil=='C' and hijos> 3 and 1975>=Año>=1965)or(Ingreso>2500000 and Estadocivil=='S' and Residencia=='C')or(Ingreso>3500000 and Añosconbanco>5)or(Residencia=='R' and hijos<2 and Estadocivil=='C')):
    print('APROBADO')

else:
    print('RECHAZADO')
             
