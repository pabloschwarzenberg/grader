#Conversión de Decimal a Binario
x=int(input("ingrese un numero:"))
lista=""
res=0
while x!=0:
    res=x%2
    x=x//2
    lista=lista+str(res)
lista=lista[::-1]
print("resultado="+str(lista))
      