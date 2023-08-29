telefono = int(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))

if 10000000 <= telefono <= 99999999 and 0 <= hora <= 23:
  if 0 <= hora <= 7:
    print('Resultado: CONTESTAR')
    
  if 8 <= hora <= 14:
    tresult = telefono%1000
    if tresult == 909:
      print('Resultado: CONTESTAR')
    else:
      print('Resultado: NO CONTESTAR')
      
  if 15 <= hora <= 16:
    print('Resultado: NO CONTESTAR')
  
  if 17 <= hora <= 19:
    tresprim = telefono//100000
    if tresprim == 877:
      print('Resultado: NO CONTESTAR')
    else:
      print('Resultado: CONTESTAR')

  if 20 <= hora <= 23:
     print('Resultado: NO CONTESTAR')

else:
  print('Uno o mas de los datos ingresados son inválidos')