#Contestador de celular
numero=input('ingrese numero telefonico: ')
z=list(map(int, str(numero)))
x=str(numero)
if len(z)==8:
  hora=int(input('ingrese hora de llamda: '))
  if 0<=hora and hora<=14:
    print('Contestar')
  elif 8<=hora and hora<=14:
    if '909' in x:
      print('Contestar')
    else:
      print('No Contestar')
  elif 17<=hora and hora<19:
    if '877' in x:
      print('No Contestar')
    else:
      print('No Contestar')
  elif 19<=hora and hora<=23:
    print('No Contestar')