'''
Este programa te contrata para programar un servicio en un banco
'''
ingresos = int(input('¿Cual es tu numero de ingresos en CLP?: '))
nacimiento = int(input('¿Cuál es tu año de nacimiento?: '))
n_hijos = int(input('¿Cuantos hijos tienes?: '))
a_pertenencia = int(input('¿Cuantos años de pertenencia tienes en el banco?: '))
estado_civil = str(input('¿Cual es tu estado civil? Utilice (S) si es soltero y (C) si es casado: '))
vivienda = str(input('¿En que sector vive? Utilice (U) si es urbano o (R) si es rural: '))



if a_pertenencia > 10 and n_hijos >= 2:
    print('APROBADO')
elif estado_civil == 'C' and n_hijos > 3 and nacimiento >= 1967 or nacimiento <= 1975:
    print('APROBADO')
elif ingresos > 2500000 and estado_civil == 'S' and vivienda == 'U':
    print('APROBADO')
elif ingresos > 3500000 and a_pertenencia > 5:
    print('APROBADO')
elif vivienda == 'R' and estado_civil == 'C' and n_hijos < 2:
    print('APROBADO')

else:
    print('RECHAZADO')