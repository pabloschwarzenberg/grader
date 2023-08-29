#Contestador de celular
numero = int(input())
hora = int(input())

if hora < 7:
  print('CONTESTAR')
elif hora < 14:
  if numero % 1000 == 909:
    print('CONTESTAR')
  else:
    print('NO CONTESTAR')
elif hora < 17:
  print('NO CONTESTAR')
elif hora < 19:
  if numero // 10**5 == 877:
    print('NO CONTESTAR')
  else:
    print('CONTESTAR')
else:
  print('NO CONTESTAR')