decimal = 0
binario = ""
decimal =int(input("ingrese el numero a convertir por favor: "))


while decimal>0:

    if (decimal%2)!=0:
        binario +="1"

    else:
        binario +="0"

    if decimal==0:
        break
    decimal = (decimal//2)
print("resultado=",(int(binario[::-1])))
   