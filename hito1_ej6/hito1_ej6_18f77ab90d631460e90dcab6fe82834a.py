#Ordenar tres números
numero1 = eval(input("Ingrese un numero"))
numero2 = eval(input("Ingrese un segundo numero"))
numero3 = eval(input("Ingrese un tercer numero"))

if(numero1<=numero2 and numero2<=numero3):
 print("{},{},{}".format(numero1,numero2,numero3))
if(numero1<=numero3 and numero3<=numero2):
  print("{},{},{}".format(numero1,numero3,numero2))
if(numero2<=numero1 and numero1<=numero3):
  print("{},{},{}".format(numero2,numero1,numero3))
if(numero2<=numero3 and numero3<=numero1):
  print("{},{},{}".format(numero2,numero3,numero1))
if(numero3<=numero1 and numero1<=numero2):
  print("{},{},{}".format(numero3,numero1,numero2))
if(numero3<=numero2 and numero2<=numero1):
  print("{},{},{}".format(numero3,numero2,numero1))