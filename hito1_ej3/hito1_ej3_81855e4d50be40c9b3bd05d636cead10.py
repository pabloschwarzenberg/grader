#Aprobación de Créditos
#2 points possible (ungraded)
#Un Banco desea implementar una política de atención automatizada de créditos de consumo, y te contrata para programar su servicio. Los postulantes entregarán al banco la siguiente información:

#Ingreso (en pesos)
#Año de nacimiento
#Número de hijos
#Años de pertenencia al banco
#Estado civil ("S": soltero, "C", casado)
#Si vive en campo o cuidad ("U": urbano, "R": rural)

#El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
#Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda.
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