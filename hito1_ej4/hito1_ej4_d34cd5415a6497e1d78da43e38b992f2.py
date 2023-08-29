x=int(input("ingrese un numero: "))
def decimal_a_binario(numero_decimal):
	numero_binario = 0
	multiplicador = 1
	while numero_decimal != 0:
		numero_binario = numero_binario + numero_decimal % 2 * multiplicador
		numero_decimal //= 2
		multiplicador *= 10
	return str(numero_binario)
print("resultado=" + decimal_a_binario(x))