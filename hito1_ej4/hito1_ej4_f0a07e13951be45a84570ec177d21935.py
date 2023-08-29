#Conversión de Decimal a Binario
num=int(input("ingrese un numero"))
binario=""

if (num>0):
  while (num>0):
    if (num%2)==0:
      binario="0"+binario
    else:
      binario="1"+ binario
    num=int(num/2)
  print("resultado="+ str (binario))
else:
    print("ingrese un numero positivo")
      