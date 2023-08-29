#Descomponer un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

unidades = numero % 10
numero = numero // 10

decenas = numero % 10
numero = numero // 10

centenas = numero % 10
numero = numero // 10

millares = numero % 10

print(millares,"M +",centenas,"C +",decenas,"D +",unidades,"U") 