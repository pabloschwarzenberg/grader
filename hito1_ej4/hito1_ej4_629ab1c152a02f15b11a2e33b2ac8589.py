#Conversión de Decimal a Binario
numero = int(input("Ingrese un numero: "))

binario = 0
i = 0
while (numero>0):
    digito  = numero % 2
    numero = int(numero//2)
    binario = binario + digito*(10**i)
    i = i + 1

print('resultado=',binario,)