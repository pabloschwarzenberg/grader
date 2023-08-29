numero_decimal = int(input("Ingrese el numero: "))
modulos = []



while numero_decimal != 0:
    modulos.insert (0, str(numero_decimal % 2))
    numero_decimal //= 2

modulos2 = ''.join(modulos)   
print("Resultado =" ,modulos2)