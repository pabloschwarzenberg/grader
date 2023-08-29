#Conversión de Decimal a Binario
numero = int(input("Ingrese un número decimal: "))
negativo = False
if numero < 0:
    negativo = True
    numero= abs(numero)
resultado = bin(numero)[2:]
if negativo:
    resultado = "-" + resultado

print(f"el resultado es = {resultado}")     