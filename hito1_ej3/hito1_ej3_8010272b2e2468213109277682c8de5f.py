#Aprobación de créditos
ingreo=int(input('Cuales son sus ingresos: '))
edad=int(input('Cual es su edad: '))
num_hijos=int(input('Cuandos ejos tiene:'))
edad_afilacion=int(input('Cuantos años tiene de afilicacion con el banco: '))
estado_civil=input('Responda"S": soltero, "C", casado: ')
domicilio=input('Responda "U": urbano, "R": rural, ')

if edad_afilacion>10 and num_hijos>=2:
    print('APROBADO')

elif estado_civil=='C' and num_hijos>3 and edad>=45 and edad<=55:
    print('APROBADO')

elif ingreo>2500000 and estado_civil=='S' and domicilio=='U':
    print('APROBADO')

elif ingreo>3500000 and edad_afilacion>5:
    print('APROBADO')

elif domicilio=='R' and estado_civil=='C' and num_hijos<2:
    print('APROBADO')

else:
    print('RECHAZADO')      