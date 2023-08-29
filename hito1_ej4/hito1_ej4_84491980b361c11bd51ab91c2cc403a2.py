#Conversión de Decimal a Binario
decimal=int(input("Inserte un numero"))
binario = ''
while decimal // 2 != 0:
 binario =str(decimal % 2)+binario
 decimal= (decimal//2)
binario=str(1)+binario
print("Resultado=",binario)