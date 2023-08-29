#Aprobación de créditos
ingresos = float(input('¿Cuál es tu ingreso? (en pesos): '))
año = int(input('Ingresa tu año de nacimiento: '))
num_hijos = int(input('¿Cuántos hijos tienes?: '))
años_p = int(input('¿Desde qué año perteneces al banco?: '))
estado = input('Ingresa tu estado civil (S soltero, C casado): ')
viviendo = input('¿Vives en campo o en ciudad? (U para urbano, R para rural): ')

if años_p > 10 and num_hijos >= 2:
  print('APROBADO')
elif estado == 'C' and num_hijos >= 3 and año > 45 and año < 55:
  print('APROBADO')
elif ingresos > 2500000 and estado == 'S' and viviendo == 'U':
  print('APROBADO')
elif ingresos > 3500000 and (año - 2023) >= 5:
  print('APROBADO') 
elif viviendo == 'R' and estado == 'C' and num_hijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')      