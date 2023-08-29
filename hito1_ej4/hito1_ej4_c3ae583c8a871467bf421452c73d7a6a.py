def calculo():
    decimal=int(input("introduce un numero"))
    binario=""
    while decimal>0:
    resto=str(decimal%2)
    binario=resto+binario
    decimal=decimal//2
print(str(binario))
