#Conversión de Decimal a Binario
numero=int(input())
binario=str("")

while(numero>=1):
  if(numero%2==0):
    x=0
  else:
    x=1
  numero=numero//2
  binario +=str(x)
  inverso=(binario[::-1])
  
print("resultado="+inverso)