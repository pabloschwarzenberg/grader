#Aprobación de créditos
ingreso = int(input())
ano_nacimiento = int(input())
numero_hijos = int(input())
anos_pertenencia = int(input())
estado_civil = input() # S soltero, C casado
campo_ciudad = input() # U urbano, R rural

if anos_pertenencia > 10 and numero_hijos >= 2:
      print('APROBADO')
elif estado_civil == 'C' and numero_hijos > 3 and (2021 - ano_nacimiento) >= 45:
      print('APROBADO')
elif estado_civil == 'C' and numero_hijos > 3 and (2021 - ano_nacimiento) <= 55:
      print('APROBADO')
elif ingreso > 2500000 and estado_civil == 'S' and campo_ciudad == 'U':
      print('APROBADO')
elif ingreso > 3500000 and anos_pertenencia > 5:
      print('APROBADO')
elif campo_ciudad == 'R' and estado_civil == 'C' and numero_hijos >= 2:
      print('APROBADO')
elif ano_nacimiento < 1975:
      print('RECHAZADO') 
elif ano_nacimiento > 1967:
      print('RECHAZADO')