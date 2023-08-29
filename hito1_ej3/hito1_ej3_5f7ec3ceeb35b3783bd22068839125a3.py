#Aprobación de créditos
año_actual = 2022
ingreso = int(input('Ingreso (en pesos): '))
año = int(input('Año de nacimiento: '))
nh  = int(input('Número de hijos: '))
apb = int(input('Años de pertenencia al banco: '))
ec  = input('Estado civil ("S": soltero, "C", casado): ')
lr  = input('Si vive en campo o cuidad ("U": urbano, "R": rural): ')
edad= año_actual - año
if apb >= 10 and nh >= 2:
    print('APROBADO')
elif ec == 'C' and nh > 3 and edad >= 45 and edad <= 55:
    print('APROBADO')
elif ingreso > 2500000 and ec == 'S' and lr == 'U':
    print('APROBADO')
elif ingreso > 3500000 and apb >= 5:
    print('APROBADO')
elif lr == 'R' and nh < 2 and ec == 'C':
    print('APROBADO')
else:
    print('RECHAZADO')