#Conversión de Decimal a Binario
numero = int(input('Introduce el número a convertir a binario: '))

decimal=str()
while numero //2 !=0:
   # decimal=str(numero % 2) + str(decimal)
    decimal=str(numero%2)+decimal
    numero = numero//2


print(("resultado=""1"+ decimal))