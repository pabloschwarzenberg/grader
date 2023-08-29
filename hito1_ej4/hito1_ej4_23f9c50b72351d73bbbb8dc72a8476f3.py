#Conversión de Decimal a Binario
num=int(input("Ingrese un número decimal: "))
binario=""
binario1=""
while num != 0:
  resto= num%2
  num=num//2
  if resto==0:
    binario +="0"    
  else:
    binario +="1"    
for i in binario:
  binario1= i+binario1 

print("resultado= ",binario1)