print('Ingrese los siguientes datos: ')

ingreso = int(input('Ingreso (en pesos): '))
nacimiento = int(input('Año de nacimiento: '))
nhijos = int(input('Número de hijos: '))
pertenencia = int(input('Años de pertenencia al banco: '))
ecivil = input('Estado civil ("S": Soltero ; "C": Casado): ')
zona = input('Zona donde vive ("U": Urbano ; "R": Rural): ')

edad = (2020 - nacimiento)

if pertenencia > 10 and nhijos >= 2:
  print('APROBADO')
elif ecivil >= "C" and nhijos > 3 and 45 < edad < 55:
  print('APROBADO')
elif ingreso > 2500000 and ecivil >= "S" and zona >= "U":
  print('APROBADO')
elif ingreso > 3500000 and pertenencia > 5:
  print('APROBADO')
elif zona >= "R" and ecivil >= "C" and nhijos < 2:
  print('APROBADO')
else:
  print('RECHAZADO')