#Conversión de Decimal a Binario
decimal=int(input("Ingrese un numero decimal: "))
def DecimalaBinario(numero):
    Binario=""
    while numero//2 !=0:
        Binario=str(numero%2) + Binario
        numero=numero//2
    return str(numero) + Binario
Valor_Binario=int(DecimalaBinario(decimal))
print("resultado=", Valor_Binario)

    