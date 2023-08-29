#Conversión de Decimal a Binario

def Decimal_Binario(n):
    Binario = []
    while n > 0:
        Binario.append(str(n % 2))
        n //= 2
    Binario.reverse()
    return ''.join(Binario)

numero = int(input("Ingrese un numero: "))
print("resultado=", Decimal_Binario(numero))