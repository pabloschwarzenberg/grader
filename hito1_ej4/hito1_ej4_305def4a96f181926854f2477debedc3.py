#Conversión de Decimal a Binario
numero = input('Ingrese su número: ')
decimal = int(numero)
respuesta = ''

while decimal > 0:
    operacion = int(decimal % 2)
    decimal = int(decimal / 2)
    respuesta = str(operacion) + respuesta
print('resultado = ', respuesta)