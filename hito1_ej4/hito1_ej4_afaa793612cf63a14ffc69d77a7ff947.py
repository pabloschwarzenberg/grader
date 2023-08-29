#Conversión de Decimal a Binario
numero = int(input("ingrese un numero"))
resultado = " "

while numero > 0:
    x = numero % 2
    numero = numero // 2
    resultado = str(x) + resultado

    print("resultado =", resultado)