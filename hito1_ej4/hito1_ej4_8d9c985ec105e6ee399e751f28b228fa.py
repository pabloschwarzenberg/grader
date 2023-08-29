#Conversión de Decimal a Binario
n=int(input("ingrese un número: "))
if n%2==0:
    binario="0"
else:
    binario="1"
    
while n>=2:
    n=n//2
    if n%2==0:
        b="0"
        binario=binario+b
    else:
        b="1"
        binario=binario+b
#int(binario)
print("resultado="+binario)