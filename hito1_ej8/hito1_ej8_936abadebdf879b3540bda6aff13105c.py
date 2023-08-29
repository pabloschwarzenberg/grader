#Descomponer un número
n = int(input('Ingrese un número de hasta cuatro dígitos: '))
if n >= 1000:
  m = n//1000
  c = (n//100) % 10
  d = (n//10) % 10
  u = n % 10
  print(m,'M',' + ',c,'C',' + ',d,'D',' + ',u,'U')
if 999 >= n >= 100:
  c = (n//100) % 10
  d = (n//10) % 10
  u = n % 10
  print(c,'C',' + ',d,'D',' + ',u,'U')
if 99 >= n >= 10:
  d = (n//10) % 10
  u = n % 10
  print(d,'D',' + ',u,'U')
if 9 >= n:
  print(n)