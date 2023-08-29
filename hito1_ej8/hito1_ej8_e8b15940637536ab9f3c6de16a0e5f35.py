#Descomponer un número

numero = int(input('Ingrese un numero hasta 4 digitos:'))
numerostr = str(numero)
len(numerostr)
if len(numerostr) == 4:
  a=(numerostr[0])
  b=(numerostr[1])
  c=(numerostr[2])
  d=(numerostr[3])
  print(a,'M','+',b,'C','+',c,'D','+',d,'U')
if len(numerostr) == 3:
  a=(numerostr[0])
  b=(numerostr[1])
  c=(numerostr[2])
  print(a,'C','+',b,'D','+',c,'U')
if len(numerostr) == 2:
  a=(numerostr[0])
  b=(numerostr[1])
  print(a,'D','+',b,'U')
if len(numerostr) == 1:
  a=(numerostr[0])
  print(a,'U')
if len(numerostr) == 0:
  print('Porfavor ingrese un numero')
if len(numerostr) > 4:
  print('Hay mas de 4 digitos')