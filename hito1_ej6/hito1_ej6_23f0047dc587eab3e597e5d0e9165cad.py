#Ordenar tres números
numero1=int(input())
numero2=int(input())
numero3=int(input())

if numero1<=numero2<=numero3:
  print("{},{},{}".format(numero1,numero2,numero3))
if numero3<=numero2<=numero1:
  print("{},{},{}".format(numero3,numero2,numero1))
if numero2<=numero3<=numero1:
  print("{},{},{}".format(numero2,numero3,numero1))
if numero3<=numero1<=numero2:
  print("{},{},{}".format(numero3,numero1,numero2))
if numero1<=numero3<=numero2:
  print("{},{},{}".format(numero1,numero3,numero2))
if numero2<=numero1<=numero3:
  print("{},{},{}".format(numero2,numero1,numero3))
