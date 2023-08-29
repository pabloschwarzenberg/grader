#Contestador de celular

numero= int(input('Ingrese numero telefonico'))
hora= int(input('Ingrese hora de la llamada (ENTRE 0 Y 23):'))
calculo1 = numero-((numero// 10**3) * 10**3)
calculo2 = (numero // 10**5)

if 7 >= hora >= 0:
  print('CONTESTAR')
while 7 < hora <= 14:
  if calculo1 == 909:
    print('CONTESTAR')
    break
  else:
   print('NO CONTESTAR')
   break
while 17 <= hora <=19:
  if calculo2 == 877:
    print('NO CONTESTAR')
    break
if hora > 19:
  print('NO CONTESTAR')