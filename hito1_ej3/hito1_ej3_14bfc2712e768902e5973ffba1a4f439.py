#Aprobación de créditos
ingreso=int(input('Cual es su ingreso?   '))
nacimiento=int(input('Cual es su año de nacimiento?   '))
Ndehijos=int(input('Cuantos hijos tiene?   '))
anos_en_el_banco=int(input('Cuantos anos lleva en el banco?   '))
print('Cual es su estado civil? ')
print('S para soltero y C para casado')
estado_civil=input('')
print('Vive en el campo o la ciudad?')
print('U si vive en el sector urbano y R si vive en el campo')
donde_vive=input('')
edad=2022-nacimiento

if anos_en_el_banco>10 and Ndehijos>=2:
    print('CREDITO APROBADO')
elif estado_civil=='C' and Ndehijos>3 and edad>=45 and edad<=55:
    print('CREDITO APROBADO')
elif ingreso>2500000 and estado_civil=='S' and donde_vive=='U':
    print('CREDITO APROBADO')
elif ingreso>3500000 and anos_en_el_banco>5:
    print('CREDITO APROBADO')
elif donde_vive=='R' and estado_civil=='C' and Ndehijos<2:
    print('CREDITO APROBADO')
else:
    print('CREDITO RECHAZADO')   