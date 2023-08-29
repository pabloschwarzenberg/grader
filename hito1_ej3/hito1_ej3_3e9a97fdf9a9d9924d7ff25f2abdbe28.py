#Aprobación de créditos
print("ingresos: ")
ingreso = int(input())
print("ingrese ano de nacimiento: ")
nacimiento = int(input())
print("ingrese cantidad de hijos: ")
hijos = int(input())
print("tiempo en el banco: ")
tiempo = int(input())
print("estado civil, Soltero = S, Casado = C ")
estado_civil= input()
print("residencia, Urbano = U, Rural = R" )
residencia = input()

ano_actual = 2022

edad = ano_actual - nacimiento

if tiempo >= 10 or hijos >= 2:
  print('APROBADO')
elif estado_civil == 'C' or hijos >= 3 or 45 < edad < 55:
  print('APROBADO')
elif ingreso >= 2500000 or estado_civil == 'S' or residencia == 'U':
  print('APROBADO')
elif ingreso >= 3500000 or tiempo > 5:
  print('APROBADO')
elif residencia == 'R' or estado_civil == 'C' or hijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')     