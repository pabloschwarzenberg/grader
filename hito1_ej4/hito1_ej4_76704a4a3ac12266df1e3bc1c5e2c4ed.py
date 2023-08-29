#Conversión de Decimal a Binario
n=int(input("ingrese un numero: "))

binario = "" 
divisor=2

while n != 0 :
  resto = n%divisor
  n = n//2
  binario += str(resto) # a += b -> a = a + b

print("resultado= ",binario[::-1])
