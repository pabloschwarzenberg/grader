numero_decimal = int(input("Ingrese un número decimal: "))
resultado = ""

while numero_decimal > 0:
    resultado = str(numero_decimal % 2) + resultado
    numero_decimal //= 2

print("resultado =", resultado)
