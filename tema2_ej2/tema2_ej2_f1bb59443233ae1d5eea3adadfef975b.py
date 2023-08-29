def amigos(a,b):
  an= 0
  bn= 0
  inc = 1
  cont = 1
  while inc < a:
      if a % inc == 0:
          an+= inc
      inc += 1
  print(an)
  while cont < b:
      if b % cont == 0:
          bn+= cont
      cont += 1
  print(bn)

  return an== b and bn== a

n1 = 220
n2 = 284

if amigos(n1,n2):
    print('Los numeros son amigos')
else:
    print('Los numeros no son amigos')