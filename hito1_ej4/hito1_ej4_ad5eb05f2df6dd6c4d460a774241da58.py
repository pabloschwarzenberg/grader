#Conversión de Decimal a Binario
numero=int(input(""))
binario=""
while numero>=1:
    if numero==1:
        binario=binario+"1"
        numero=0
    elif numero%2==0:
        binario=binario+"0"
        numero=numero//2
    elif numero%2!=0:
        binario=binario+"1"
        numero=numero//2
binario=binario[::-1]
print("resultado="+str(binario))  