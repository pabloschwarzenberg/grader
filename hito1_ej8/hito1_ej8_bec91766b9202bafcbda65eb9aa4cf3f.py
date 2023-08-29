#Descomponer un número
numero = int(input('Ingresa un valor de hasta 4 digitos: '))
if 0<numero<10000:
  mil = numero//1000
  centena = (numero%1000)//100
  decena = ((numero%1000)%100)//10
  unidad = ((numero%1000)%100)%10
  print(mil,'M +',centena,'C +',decena,'D +',unidad,'U')
else:
  print('Debe ser un numero de hasta 4 cifras')
