#Conversión de Decimal a Binario
n=int(input("ingrese un numero: "))
lista=("")
while (n>=1):
 if(n%2==0):
  lista+="0"
  n=n/2
 else:
   lista += "1"
   n=int(n/2)
lista0=int(str(lista[::-1]))
print ("resultado=", lista0)