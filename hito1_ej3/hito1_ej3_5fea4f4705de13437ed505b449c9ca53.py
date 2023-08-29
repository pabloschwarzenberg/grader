#Aprobación de créditos
ingreso=eval(input('Registre su ingreso: '))
nacim=eval(input('Registre el año de nacimiento: '))
hijos=eval(input('Registre número de hijos: '))
antiguedad=eval(input('Registre años de antiguedad en el banco: '))
estado_civil=input('Registre su estado civil(S/C): ')
ubicacion=input('Registre si vive en campo o ciudad(U/R): ')

edad=2020-nacim

if antiguedad>10 and hijos >=2:
    print('APROBADO')
elif estado_civil=="C"and hijos > 3 and edad>=45 and edad<=55:
    print('APROBADO')
elif ingreso>2500000 and estado_civil=="S" and ubicacion=="U":
    print('APROBADO')
elif ingreso>3500000 and antiguedad >5:
    print('APROBADO')
elif ubicacion=="R" and estado_civil=="C" and hijos<2:
    print('APROBADO')
else:
    print('RECHAZADO')      