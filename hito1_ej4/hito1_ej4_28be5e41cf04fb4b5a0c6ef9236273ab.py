numero_decimal_str= input('ingrese numero decimal')

numero_decimal_str = numero_decimal_str.replace(',','.')

numero_decimal = float(numero_decimal_str)

binario_entero = bin(int(numero_decimal))[2:]

print('resultado=',binario_entero)