#Descomponer un número
numero=input("Ingrese un número: ")
A=numero[:1]
V=numero[1:2]
C=numero[2:3]
D=numero[3:4]
numero=int(numero)
if numero>999:
  print(A,"M","+",V,"C","+",C,"D","+",D,"U")
else:
  if 99<numero<1000:
    print(A,"C","+",V,"D","+",C,"U")
  else:
    if 9<numero<100:
      print(A,"D","+",V,"U")
    else:
      if numero<10:
        print(A,"U")      