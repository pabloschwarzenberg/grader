numero = int(input("Introduzca Numero:"))

M = numero / 1000
tmp = numero % 1000

C = tmp / 100
tmp = tmp % 100


D = tmp / 10


U = tmp % 10


if numero > 1000:
  print ("%i"%M,"M","+","%i"%C,"C","+","%i"%D,"D","+","%i"%U,"U")
if numero < 1000 and numero >= 100:
  print ("%i"%C,"C","+","%i"%D,"D","+","%i"%U,"U")
if numero < 100 and numero >= 10:
  print ("%i"%D,"D","+","%i"%U,"U")
if numero < 10:
  print ("%i"%U,"U")

      