#Aprobación de créditos
ingreso = eval(input('Ingreso (en pesos):'))
año = eval(input('Año de nacimiento:'))
hijos = eval(input('Número de hijos:'))
añosbanco = eval(input('Años de pertenencia al banco:'))
escivil = input('Estado civil ("S": soltero, "C", casado):')
zona = input('¿Vive en campo o cuidad? ("U": urbano, "R": rural):')
print('\n')

edad = 2020-año

if añosbanco >= 10 and hijos >= 2:
    print('APROBADO')
elif escivil=='C' and hijos > 3 and 45 < edad <55:
    print('APROBADO')
elif ingreso < 2500000 and escivil == 'S' and zona == 'u':
    print('APROBADO')
elif ingreso < 3500000 and añosbanco > 5:
    print('APROBADO')
elif zona == 'R' and escivil == 'C' and hijos <= 2:
    print('APROBADO')
else:
    print('RECHAZADO')
