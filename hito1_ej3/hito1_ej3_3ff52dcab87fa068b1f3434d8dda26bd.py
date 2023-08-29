Ingresos=int(input('monto de tu ingreso: '))
Nacimiento=int(input('ingresa el ano de nacimiento: '))
Hijos=int(input('ingresa cuantos hijos tienes: '))
Pertenencia=int(input('cuantos años llevas con el banco: '))
Estadocivil=str(input('ingresa ,S, si estas soltero/a o ,C, si estas casado/a: '))
Dondevive=str(input('ingresa ,U, si es urbano o ,R, si es rural: '))

Edad=(2020-Nacimiento)

if (10 <= Pertenencia and Hijos>= 2) or (Estadocivil == 'C' and Hijos>= 3 and 45<= Edad <=55)\
   or (Ingresos > 2500000 and Estadocivil == 'S' and Dondevive == 'U')\
   or (Ingresos > 3500000 and Pertenencia > 5) or (Dondevive == 'R' and Estadocivil == 'C' and Hijos < 2):
    print('APROBADO')
else:
  print('RECHAZADO')