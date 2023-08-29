#Aprobación de créditos
rechazo=False
#esto no lo debes ingresar, debiera ser una constante
year=2018
ingreso=input('Ingrese su sueldo mensual:')
ingreso=int(ingreso)
print('*')
nacimiento=input('Ingrese su año de nacimiento:')
nacimiento=int(nacimiento)
print('*')
hijos=input('Ingrese el numero de hijos que tiene:')
hijos=int(hijos)
print('*')
pertenencia_al_banco=input('Ingrese la cantidad de años que lleva en este banco:')
pertenencia_al_banco=int(pertenencia_al_banco)
print('*')
estado_civil=input('Ingrese su estado civil, Casado o Soltero [C/S]:')
print('*')
vivienda=input('Indique si vive en una zona rural o urbana [R/U]:')
print('*')
print('*')

edad=year-nacimiento
if hijos>=2 and pertenencia_al_banco>10:
    print('APROBADO')
else:

 if estado_civil=='C' and hijos>3 and edad>=45 and edad<=55:
    print('APROBADO')
 else:

  if estado_civil=='S' and ingreso>2500000 and vivienda=='C':
    print('APROBADO')
  else:

   if ingreso>3500000 and pertenencia_al_banco>5:
    print('APROBADO')
   else:
 
     if vivienda=='R' and hijos<2:
         print('APROBADO')
     else:
#el mensaje debiera ser RECHAZADO
         print('RECHAZADO')
