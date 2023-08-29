#Aprobación de créditos
#Datos del cliente
ingreso=int(input())
nacimiento=int(input())
fecha_actual=2018
edad=fecha_actual-nacimiento
num_hijos=int(input())
t_pertenencia=int(input())
est_civil=str(input())
lug_vivienda=str(input())
#Condición 
if t_pertenencia>10 and num_hijos>=2:
   print('APROBADO')
elif est_civil=='C' and num_hijos>=3 and 45<edad and edad<55:
  print('APROBADO')
elif ingreso>2500000 and est_civil==S and lug_vivienda==U:
  print('APROBADO')
elif ingreso>3500000 and t_pertenecia>5:
  print('APROBADO')
elif lug_vivienda=='R' and est_civil=='C' and num_hijos<2:
  print('APROBADO')
else:
  print('RECHAZADO')