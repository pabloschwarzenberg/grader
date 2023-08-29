#Aprobación de créditos
ingreso = int(input('ingresos: '))
nacimiento = int(input('ingrese ano de nacimiento: '))
hijos = int(input('ingrese cantidad de hijos: '))
tiempo = int(input('tiempo en el banco: '))
estado_civil= input(' estado civil, Soltero = S, Casado = C' )
residencia = input(' residencia, Urbano = U, Rural = R' )
ano_actual = 2022
edad = ano_actual - nacimiento

if tiempo >= 10 and hijos >= 2:
  print('APROBADO')
elif estado_civil == 'C' and hijos >= 3 and 45 < edad < 55:
  print('APROBADO')
elif ingreso >= 2500000 and estado_civil == 'S' and residencia == 'U':
  print('APROBADO')
elif ingreso >= 3500000 and tiempo > 5:
  print('APROBADO')
elif residencia == 'R' and estado_civil == 'C' and hijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')      