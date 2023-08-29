#Aprobación de créditos
ingreso=int(input('ingrese su ingreso mensual: '))
nac=int(input('ingrese su año de nacimiento: '))
hijos=int(input('cantidad de hijos: '))
pert=int(input('ingrese sus años de pertenencia al banco: '))
estado=input('ingrese su estado civil (S= soltero),(C= casado): ')
lugar=input('ingrese U si vive en ciudad o R si vive en el campo: ')
edad= 2020-nac

if pert > 10 and hijos>=2:
  print('APROBADO')
elif estado == 'S' and hijos > 3 and 55>edad>45:
  print('APROBADO')
elif ingreso > 2500000 and estado == 'S'  and lugar == 'U':
  print('APROBADO')
elif ingreso > 3500000 and pert > 5:
  print('APROBADO')
elif lugar == 'R' and estado == 'C' and hijos < 2:
  print('APROBADO')

else:
  print('RECHAZADO')








