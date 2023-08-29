#Aprobación de créditos
ingresos = int(input('Ingresos: '))
año_nacimiento = int(input('Año de nacimiento: '))
numero_hijos = int(input('Numero de hijos: '))
años_en_banco = int(input('Años de pertenencia al banco: ')) 
estado_civil = str(input('Estado civil ( "S": soltero, "C": casado): '))
casa = str(input('Ubicacion de su casa ("U": urbano, "R": rural): '))

edad= 2020 - año_nacimiento

if años_en_banco > 10 and numero_hijos >= 2:
    print('APROBADO')
if estado_civil == 'C' and numero_hijos > 3 and 45 <= edad <= 55:
    print('APROBADO')
if ingresos > 2500000 and estado_civil == 'S' and casa == 'U':
    print('APROBADO')
if ingresos > 3500000 and años_en_banco > 5:
    print('APROBADO')
if casa == 'R' and estado_civil == 'C' and numero_hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')