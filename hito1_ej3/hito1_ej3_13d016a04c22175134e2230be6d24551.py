#Aprobación de créditos
ingreso=int(input('Ingreso:'))
ano_nacimiento=int(input('Año de nacimiento:'))
numero_de_hijos=int(input('Número de hijos:'))
anos_de_pertenencia=int(input('Años de pertenencia al banco:'))
estado_civil=input('Estado civil: Coloque S si es soltero, o C si es casado:')
vivienda=input('Vivienda: Coloque U si es urbano, o R si es rural:')

if anos_de_pertenencia > 10 and numero_de_hijos >= 2:
    print ('APROBADO')
if estado_civil == "C" and ano_nacimiento >= 1963 and ano_nacimiento <= 1973:
    print ('APROBADO')
if  ingreso > 2500000 and estado_civil == 'S' and vivienda == 'U':
    print ('APROBADO')
if ingreso > 3500000 and anos_de_pertenencia >5:
    print ('APROBADO')
if vivienda == 'R' and estado_civil== 'C' and numero_de_hijos < 2:
    print ('APROBADO')
else:
    print ('RECHAZADO')