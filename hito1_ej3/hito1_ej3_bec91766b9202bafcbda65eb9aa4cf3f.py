#Aprobación de crédito
#Asignacion de variables
ingreso = int(input('Monto de ingresos (en pesos): '))
nacimiento = int(input('Ingrese su ano de nacimiento: '))
num_hijos = int(input('Ingrese la cantidad de hijos: '))
pertenencia = int(input('Ingrese los anos de pertenencia al banco: '))
estado_civil = str(input('Ingrese su estado civil, "S" si es Soltero o "C" si es Casado: '))
vivienda = str(input('Ingrese si vive en Campo o ciudad, "U" de Urbano o "R" de Rural: '))
edad = nacimiento - 2022

#Para decidir la aprobacion del credito

if pertenencia > 10 and num_hijos >= 2:
  print('APROBADO')
elif estado_civil == 'C' and num_hijos > 3 and edad > 45 and edad < 55:
  print('APROBADO')
elif ingreso > 2500000 and estado_civil == 'S' and vivienda == 'U':
  print('APROBADO')
elif ingreso == 3500000 and pertenencia > 5:
  print('APROBADO')
elif vivienda == 'R' and estado_civil == 'C' and num_hijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')