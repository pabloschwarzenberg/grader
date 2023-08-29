dec=int(input("Ingrese un numero entero Decimal: "))
i=0
resto=0
binario=""
while (binario!="1"):
    if((dec//(2**(i)))==1):
        resto=dec-(2**i)
        binario="1"
    else:
        i=i+1
while (i!=0):
        i=i-1
        if((resto//(2**i))==1):
            binario=binario +"1"
            resto=resto-(2**i)
        else:
            binario= binario +"0"
print("resultado=",binario)