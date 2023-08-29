#Conversión de Decimal a Binario
decimal = float(input('Ingrese un número decimal: '))
lista = []
while decimal > 0:
    resto = int(decimal % 2)
    decimal = int(decimal / 2)
    lista.append(resto)
binario = list(reversed(lista))
print('resultado=',*binario, sep= "")
