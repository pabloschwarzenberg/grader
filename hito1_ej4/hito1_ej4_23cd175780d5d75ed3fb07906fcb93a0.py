#Conversión de Decimal a Binario
decimal=int(input("Ingrese un número positivo"))
binario=""
while(decimal>0):
    if(decimal%2==0):
        binario="0"+binario
    else:
        binario="1"+binario
    decimal=decimal//2

print("El numero en binario es: ", eval(binario))