#Aprobación de créditos

ingresos = int(input('\nIngresos: '))
año_nacimiento = int(input('Año de Nacimiento: '))
hijos = int(input('N° de Hijos: '))
años_banco = int(input('Años de pertenencia en el benaco: '))
estado_civil = input('Estado civil (S: Soltero/C: Casado): ')
lugar = input('Campo o Ciudad (U: Urbano/R: Rural): ')
edad = 2022-año_nacimiento

if años_banco>10 and hijos>=2:
    print('\nAPROBADO')
elif (estado_civil=='C' or estado_civil=='c') and hijos>4 and edad>=45 and edad<=55:
    print('\nAPROBADO')
elif ingresos>2500000 and (estado_civil=='C' or estado_civil=='c') and (lugar=='U' or lugar=='u'):
    print('\nAPROBADO')
elif ingresos>3500000 and años_banco>5:
    print('\nAPROBADO')
elif (lugar=='R' or lugar=='r') and (estado_civil=='C' or estado_civil=='c') and hijos<2:
    print('\nAPROBADO')
else:
    print('\nRECHAZADO')