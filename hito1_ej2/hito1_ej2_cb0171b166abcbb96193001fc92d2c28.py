#Contestador de celular
numero = int(input('ingrese numero telefonico:'))
llamada = int(input('ingrese hora de la llamada:'))

if (0 <= llamada <= 7):
 print('Resultado: CONTESTAR ')
else:
 if llamada <= 14 and numero%1000 == 909:
  print('Resulatado: CONTESTAR')
 else:
  if llamada <= 14:
   print('Resultado: NO CONTESTAR')  
  else:
    if 17<= llamada <=19 and numero//87700000 == 1:
     print('Resulatdo: NO CONTESTAR')
    else:
     if 17<= llamada <=19:
      print('Resulatado: CONTESTAR')
     else:
       if llamada >= 19:
        print('Resultado: NO CONTESTAR')
        