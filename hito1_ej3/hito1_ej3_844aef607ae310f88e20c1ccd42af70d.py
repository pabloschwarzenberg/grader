#Aprobación de créditos
ingre = int(input('Ingrese su ingreso monetario (en pesos):'))
naci = int(input('Ingrese su año de nacimiento: '))
hijo = int(input('Ingrese la cantidad de hijos que tiene: '))
anio = int(input('Ingrese los años de pertenencia al banco que tiene: '))
estado = input('Ingrese su estado civil ("S": soltero, "C": casado): ')
vive = input('Ingrese donde vive ("U": Urbano, "R": Rural): ')

if anio>10 and hijo>=2:
  print('APROBADO')
elif estado =='C' and hijo>3 and naci>=1975 and naci>=1965:
  print('APROBADO')
elif ingre>2500000 and estado == 'S' and vive == 'U':
  print('APROBADO')
elif ingre>3500000 and anio>5:
  print('APROBADO')
elif vive=='R' and hijo<2:
  print('APROBADO')
else:
  print('RECHAZADO')