ingreso=int(input('ingreso: '))
añonac=int(input('Ingrese año de nacimiento: '))
hijos=int(input('Numero de hijos: '))
añosbanca=int(input('Ingrese Años en la banca: '))
estadocivil=str(input('Ingrese S, Soltero o C, casado :'))
lugar=str(input('Ingrese U, urbano o R, rural :'))
if añosbanca > 10 and hijos >= 2:
    print('APROBADO')
if estadocivil == 'C' and hijos > 3 and 45<añonac<55:
    print('APROBADO')
if ingreso>2500000 and estadocivil == 'S' and lugar == 'U':
    print('APROBADO')
if ingreso>3500000 and añosbanca > 5:
    print('APROBADO')
if lugar == 'R' and estadocivil == 'C' and hijos < 2:
    print('APROBADO')
print('RECHAZADO')
