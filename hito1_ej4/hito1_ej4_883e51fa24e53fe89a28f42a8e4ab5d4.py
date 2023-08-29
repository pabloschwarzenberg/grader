#Conversión de Decimal a Binario
def to_binary(num):
    binary_digits = []
    while num > 0:
        binary_digits.insert(0, str(num % 2))
        num = num // 2
    binary = ''.join(binary_digits)
    return binary

num_decimal = int(input("Ingrese un número decimal: "))
num_binario = to_binary(num_decimal)
print("resultado =", num_binario)

      