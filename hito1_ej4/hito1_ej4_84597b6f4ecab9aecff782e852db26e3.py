#Conversión de Decimal a Binario
n=int(input("ingrese numero"))
n2=n%2
if n2 ==0:
    binario="0"
else:
    binario="1"
n=n//2
while n >0:
    n2=n%2
    if n2 ==0:
        binario="0" + binario
    else:
        binario="1" + binario
    n=n//2
print("resultado=", binario)
        