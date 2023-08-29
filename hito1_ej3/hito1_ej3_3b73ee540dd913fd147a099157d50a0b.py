#Aprobación de créditos
ingreso = 0
año_nac = 0
hijos = 0
años_banco = 0
estado_civil = 0
vivienda = 0

ingreso = int(input('Cual es su ingrso(En Pesos): '))
año_nac = int(input('Ingrese su año de naciemiento (Completo): '))
hijos = int(input('Numero de hijos: '))
años_banco = int(input('Hace cuantos años pertenece al banco ?: '))
estado_civil = str(input('Estado civil ("S": soltero, "C", casado): '))
vivienda = str(input('Si vive en campo o cuidad ("U": urbano, "R": rural): '))
formula_año_nac = 2021 - año_nac
if años_banco > 10 and hijos >= 2:
    print('APROBADO')
elif estado_civil == 'C' and hijos > 3 and formula_año_nac >= 45 and formula_año_nac <= 55:
    print ('APROBADO')
elif ingreso > 2500000 and estado_civil == 'S' and vivienda == 'U':
    print ('APROBADO')
elif ingreso > 3500000 and años_banco > 5:
    print ('APROBADO')
elif vivienda == 'R' and estado_civil == 'C' and hijos < 2:
    print ('APROBADO') 
else:
    print('NO APROBADO')