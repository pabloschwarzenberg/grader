#Aprobación de créditos
ingreso = int(input())
ano_nacimiento = int(input())
numero_hijos = int(input())
anos_pertenencia = int(input())
estado_civil = input() # S soltero, C casado
campo_ciudad = input() # U urbano, R rural

if anos_pertenencia > 10 and numero_hijos >= 2:
    print('APROBADO')
elif estado_civil == 'S' and numero_hijos > 3 and (2021 - ano_nacimiento) >= 45 and (2021 - ano_nacimiento) <=55:
    print('APROBADO')
elif ingreso > 2500000 and estado_civil == 'S' and campo_ciudad == 'U':
    print('APROBADO')
elif ingreso > 3000000 and anos_pertenencia > 5:
    print('APROBADO')
elif campo_ciudad == 'R' and estado_civil == 'C' and numero_hijos < 2:
    print('APROBADO')
else:
    print('RECHAZADO')    