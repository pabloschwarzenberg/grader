# completa el código de la función
def amigos(a,b):
  anum = 0
  bnum = 0
  i = 1
  j = 1
  while i < a:
      if a % i == 0:
          anum += i
      i += 1
  print(anum)
  while j < b:
      if b % j == 0:
          bnum += j
      j += 1
  print(bnum)

  return anum == b and bnum == a

#n1 = int(input('Ingrese un numero A: '))
#n2 = int(input('Ingrese un numero B: '))
n1 = 220
n2 = 284

if amigos(n1,n2):
    print('Los numeros son amigos')
else:
    print('Los numeros no son amigos')
           