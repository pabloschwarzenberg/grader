#Descomponer un número
num = int(input('Ingresa un numero de hasta 4 digitos:\n'))

mil = num // 1000 % 10
cen = num // 100 % 10
dec = num // 10 % 10
uni = num // 1 % 10

print(str(mil)+'M','+', str(cen)+'C','+', str(dec)+'D','+', str(uni)+'U')