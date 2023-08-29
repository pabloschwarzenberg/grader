#Descomponer un número
numero = int(input("ingresa un numero : "))

unidades = numero%10
numero = numero//10

decenas = numero%10
numero = numero//10

centenas = numero%10
numero = numero//10

unidadesmil = numero%10

print(f"\Descomposicion:{unidadesmil}M + {centenas}C + {decenas}D + {unidades}U\n")
