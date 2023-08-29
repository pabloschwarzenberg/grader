#Aprobación de créditos
ingreso = int(input('Ingreso (en pesos): '))
ano_nacimiento = int(input('Año de nacimiento: '))
n_hijos = int(input('Número de hijos: '))
anos_banco = int(input('Años de pertenencia al banco: '))
estado_civil = input('Estado civil ("S": soltero, "C", casado): ').upper()
vivienda = input('Vive en campo o cuidad ("U": urbano, "R": rural): ').upper()
if anos_banco >= 10 and n_hijos >= 2:
    print('APROBADO')
elif estado_civil == 'C' and n_hijos >= 3 and (ano_nacimiento >= 1966 or ano_nacimiento <= 1976):
    print('APROBADO')
elif ingreso > 2500000 and estado_civil == 'S' and (vivienda) == 'U':
    print('APROBADO')
elif ingreso > 3500000 and anos_banco > 5:
    print('APROBADO')
elif vivienda == 'R' and estado_civil == 'C' and n_hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')