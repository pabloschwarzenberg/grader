#Aprobación de créditos
ingreso=int(input('Ingrese los ingresos en pesos: '))
año=int(input('Ingrese el año de nacimiento: '))
hijos=int(input('Ingrese el número de hijos: '))
añobanco=int(input('Ingrese los años que lleva en el banco: '))
estado=input('Ingrese estado civil, soltero(S) o Casado(C): ')
vive=input('Ingrese si vive en campo(R) o ciudad(U): ')

if añobanco>10 and 2<=hijos:
    print('APROBADO.')
elif estado=='C' and hijos>3 and 1964<=año<=1974:
    print('APROBADO.')
elif ingreso>2500000 and estado=='S'and vive=='U':
    print('APROBADO.')
elif ingreso>3500000 and añobanco>5:
    print('APROBADO.')
elif vive=='R' and estado=='C'and hijos<2:
    print('APROBADO.')
else:
    print('RECHAZADO.')
