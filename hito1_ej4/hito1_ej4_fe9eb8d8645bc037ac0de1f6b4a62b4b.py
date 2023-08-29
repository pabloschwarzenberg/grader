#Conversión de Decimal a Binario
n=int(input("numero: "))
seguir=True
while seguir:
  resto=int(n%2)
  n=n//2
  if n==0:
    seguir=False
print("resultado=",resto)
    
  
  
