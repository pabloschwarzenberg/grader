#Aprobación de créditos
ingreso = int(input('Ingreso (en pesos): '))
anoDeNacimiento = int(input('Año de nacimiento: '))
numeroHijos = int(input('Número de hijos: '))
anoPertenencia = int(input('Años de pertenencia al banco: '))
estadoCivil = input('Estado civil ("S": soltero, "C", casado): ')
vivienda = input('Si vive en campo o cuidad ("U": urbano, "R": rural): ')

mensaje = 'RECHAZADO'
if anoPertenencia > 10 and numeroHijos >= 2:
    mensaje = 'APROBADO'
if estadoCivil == 'S' and numeroHijos >= 3 and 45 <= (2020-anoDeNacimiento) <= 55:
    mensaje = 'APROBADO'
if ingreso > 2500000 and estadoCivil == 'S' and vivienda == 'U':
    mensaje = 'APROBADO'
if ingreso > 3500000 and anoPertenencia > 5:
    mensaje = 'APROBADO'
if vivienda == 'R' and estadoCivil == 'C' and numeroHijos < 2:
    mensaje = 'APROBADO'

print(mensaje)