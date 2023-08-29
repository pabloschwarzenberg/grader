#Ordenar tres números
n1 = int(input("inserte el primer número:  "))
n2 = int(input("inserte el segundo número:  "))
n3 = int(input("inserte el tercer número:  "))

primero = None
segundo = None
tercero = None

if n1>n2 and n1>n3:
  primero = n1
  if n2>n3:
    segundo = n2
    tercero = n3
  else:
    segundo = n3
    tercero = n2
elif n3>n2 and n3>n1:
  primero = n3
  if n2>n1:
    segundo = n2
    tercero = n1
  else:
    segundo = n1
    tercero = n2
elif n2>n1 and n2>n3:
  primero = n2
  if n1>n3:
    segundo = n1
    tercero = n3
  else:
    segundo = n3
    tercero = n1
else:
  print("dos o más números son iguales")
  
print(tercero, segundo, primero)  