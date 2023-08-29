#Conversión de Decimal a Binario
decimal = int(input('Introduce el número a convertir a binario: '))
res = bin(decimal)
print("resultado=", res[2:])      