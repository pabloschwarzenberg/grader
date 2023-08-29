#Contestador de celular
numero=int(input('ingrese numero:'))
hora=eval(input('ingrese hora de llamada:'))

##print(numero)
if (len(str(numero)) == 8) and (hora >= 0 and hora <= 23):
  if hora >  7 and hora < 14 and numero%1000 != 909:
   print('NO CONTESTAR')
  elif (hora >=  17 and hora <= 19 and int(numero/100000) != 877) or (hora >=  0 and hora <= 7) or (hora >  7 and hora < 14 and int(numero%1000) == 909): 
   print('CONTESTAR')
  else:
   print('NO CONTESTAR')
else:
  print('DEBE INGRESAR UN NUMERO DE 8 DIGITOS Y HORA ENTRE LAS 0 Y 23')
  