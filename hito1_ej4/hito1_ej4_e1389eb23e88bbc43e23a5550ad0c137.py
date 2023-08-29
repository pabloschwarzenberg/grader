#Conversión de Decimal a Binario
n=int(input("Ingrese numero"))
binario= ""
while n!= 1:
  binario= binario + str(n%2)
  n= n//2
  if n==1:
    binario = binario + '1'
print ("resultado=",binario[::-1])

  