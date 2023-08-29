print('Bienvenido al Banco')
ingresos = int(input('\nCuales son sus ingresos?: '))
nacimiento = int(input('\nCual es su año de nacimiento?:'))
hijos = int(input('\nCuantos hijos tiene?: '))
años_banco = int(input('Cuantos años ha pertenecido al banco?: '))
e_civil = input(
                'Cual es su estado civil?'
                '\nS.- Soltero'
                '\nC.- Casado'
                ''
                )
vivienda = input('En donde vive?'
                 '\nU.- Urbano o ciudad'
                 '\nR.- Rural o campo'
                 ''
                 )

if años_banco >= 10 and hijos >= 2:
    print('\nAPROBADO')
elif e_civil == 'C' and hijos >= 3 and nacimiento >= 1968 and nacimiento <= 1978:
    print('\nAPROBADO')
elif ingresos >= 2500000 and e_civil == 'S' and vivienda == 'U':
    print('\nAPROBADO')
elif ingresos >= 3500000 and años_banco >= 5:
    print('\nAPROBADO')
elif vivienda == 'R' and e_civil == 'C' and hijos <= 2:
    print('\nAPROBADO')
else:
    print('\nRECHAZADO')
      