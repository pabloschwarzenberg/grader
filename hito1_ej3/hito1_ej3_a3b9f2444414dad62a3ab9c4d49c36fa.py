#Aprobación de créditos
ingresos=int(input('Ingrese su sueldo: ')) 
anos_de_nacimiento=int(input('Ingrese su año de nacimiento: '))
numero_de_hijos=int(input('Ingrese su numero de hijos: ')) 
anos_pertenencia_banco=int(input('Ingrese los años de pertencia al banco: '))
estado_civil=input('Ingrese su estado civil ("S":soltero/a,"C":Casado/a): ')
vivienda=input('Ingrese su tipo de vivienda ("U":urbano,"R":rural): ')


if anos_pertenencia_banco>10 and numero_de_hijos>=2:
  print('APROBADO')
elif estado_civil=='C' and numero_de_hijos>3 and 1977<anos_de_nacimiento<1967:
  print('APROBADO')
elif ingresos>2500000 and estado_civil=='S' and vivienda=='U':
  print('APROBADO')
elif ingresos>3500000 and anos_pertenencia_banco>5:
  print('APROBADO')
elif vivienda=='R' and estado_civil=='C' and numero_de_hijos<2:
  print('AAPROBADO')
else:
  print('RECHAZADO')      