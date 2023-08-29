numero_decimal = int(input("ingrese su numero"))

resultado = 0
multiplicador = 1

while numero_decimal != 0:
    resultado = resultado + numero_decimal % 2 * multiplicador
    numero_decimal //= 2 
    multiplicador *= 10 

print("resultado=", resultado)

