numero = int(input("Ingresa un número de 4 cifras: "))
unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
miles = numero%10
print("{miles}M + {centenas}C + {decenas}D+ {unidades}U")