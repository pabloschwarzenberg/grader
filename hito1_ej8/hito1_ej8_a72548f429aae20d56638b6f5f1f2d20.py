#Descomponer un número
numero = eval(input("Introduce un número"))

mil = numero // 1000
div = numero % 1000
cen = div // 100
div = div % 100
dec = div // 10
div = div % 10
uni = div // 1
div = div % 1

print(mil, "M+", cen, "C+", dec, "D+", uni, "U")