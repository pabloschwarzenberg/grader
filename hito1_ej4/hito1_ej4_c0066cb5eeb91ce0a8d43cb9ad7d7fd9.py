#Conversión de Decimal a Binario
numero=int(input())

binario= ""

while numero != 0:
  resto= numero%2
  numero=numero//2
  binario +=str(resto)    
print("resultado= ",binario[::-1])