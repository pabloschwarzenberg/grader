#Contestador de celular

telefono=int(input('Ingresa numero telefonico de 8 digitos: '))
hora= int(input('Ingrese hora de la llamada entre 0 a 23: '))

print('\n')

if 10000000<=telefono<=99999999 and 0<=hora<=23:

  if 0<=hora<=7:
    print('Resultado: Contestar')
  if 7<hora<14 and telefono%1000!=909:
    print('Resultado: No contestar')
  if 7<hora<14 and telefono%1000==909:
    print('Resultado: Contestar')
  if 14<=hora<17:
    print('Resultado: No contestar')
  if 17<=hora<=19 and telefono//100000!=877:
    print('Resultado: Contestar')
  if 17<=hora<=19 and telefono//100000==877:
    print('Resultado: No contestar')
  if 19<hora<=23:
    print('Resultado: No contestar')
 
else:
  print('Informacion ingresada erroneamente')