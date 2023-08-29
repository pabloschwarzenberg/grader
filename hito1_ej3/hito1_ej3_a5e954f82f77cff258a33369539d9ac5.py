#Aprobación de créditos
ing=eval(input('Ingresa la cantidad de ingreso: '))
an=eval(input('Ingresar año nacimiento: '))
nh=eval(input('Ingresa el numero de hijos: '))
apb=eval(input('Ingresa la cantidad de años de pertenencia al banco: '))
ec=input('Ingrese estado civil (S:Soltero, C:Casado): ')
c=input('Ingresar si vive en campo (R) o ciudad (U): ')
ed=abs(an-2020)
if apb>=10 and nh>=2:
  print('APROBADO')
elif ec=='C' and nh>=3 and (ed>=45 and ed<=55):
  print('APROBADO')
elif ing>=2500000 and ec=='S' and c=='U':
  print('APROBADO')
elif ing>=3500000 and apb>5:
  print('APROBADO')
elif c=='R' and ec=='C' and nh<2:
  print('APROBADO')
else:
  print('REPROBADO')