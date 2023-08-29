numero = int(input ('ingrese un numero de 4 cifras'))

umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print (int (umil),'M+',int (centenas),'C+', int (decenas), 'D+', int (unidades), 'U')
      