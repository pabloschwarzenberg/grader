#Descomponer un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))
unidades = numero % 10
numero //= 10
decenas = numero % 10
numero //= 10
centenas = numero % 10
numero //= 10
miles = numero % 10
numero //= 10
print(miles,'M+' centenas,'C+', decenas,'D+', unidades'U+')    