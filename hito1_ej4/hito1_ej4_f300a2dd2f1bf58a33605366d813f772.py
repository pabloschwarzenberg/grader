#Conversión de Decimal a Binario      
nro=int(input())
binario=""
while nro>0:
    if nro%2==0:
        binario="0"+binario
    else:
        binario="1"+binario
    nro=nro//2
print ("resultado="+str(binario))
    