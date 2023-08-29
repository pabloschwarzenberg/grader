#Conversión de Decimal a Binario
dec=int(input("ingrese número entero positivo: "))
maximo=0
binario=""
for i in range(30,-1,-1):
    if (dec//(2**i))==1:
        maximo=i
        break
resto=dec
for i in range(maximo,-1,-1):
    if (resto//(2**i))==1:
        resto=resto-(2**i)
        binario=binario+"1"
    else:
        binario=binario+"0"
print("resultado=",int(binario))  