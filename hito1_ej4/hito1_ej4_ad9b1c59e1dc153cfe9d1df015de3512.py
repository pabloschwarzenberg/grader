def binario(decimal):
    binario=decimal%2
    while decimal//2>0:
        decimal=decimal//2
        binario=str(decimal%2)+str(binario)
    return binario
a=int(input("ingrese numero que desea convertir a binario: "))
print("resultado= ",binario(a))
