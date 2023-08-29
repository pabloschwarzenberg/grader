#Factores Primos
x = int(2)
numero = int(input("Ingrese un numero a convertir : "))

while numero != 1:
  if (numero % x == 0):
   print(str(x)+ " ")
   numero /= x
  else:
    x += 1
  