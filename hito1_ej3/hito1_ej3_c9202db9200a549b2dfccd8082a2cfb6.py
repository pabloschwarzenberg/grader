#Aprobación de créditos
pesos = int(input('Ingreso (en pesos): '))
nacimiento = int(input('Año de nacimiento: '))
hijos = int(input('Número de hijos: '))
aniosPertenencia = int(input('Años de pertenencia al banco: '))
estadoCivil = input('Estado civil ("S": soltero, "C", casado): ')
vivienda = input('Si vive en campo o cuidad ("U": urbano, "R": rural): ')

edad = 2021 - nacimiento

if aniosPertenencia > 10 and hijos >= 2:
    print('APROBADO')

elif estadoCivil == 'C' and hijos > 3 and Edad > 45 and edad <=55:
    print('APROBADO')

elif pesos > 2500000 and estadoCivil == 'S' and vivienda == 'U':
    print('APROBADO')

elif pesos > 3500000 and añosPertenencia > 5:
    print('APROBADO')

elif vivienda == 'R' and estadoCivil == 'C' and hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')