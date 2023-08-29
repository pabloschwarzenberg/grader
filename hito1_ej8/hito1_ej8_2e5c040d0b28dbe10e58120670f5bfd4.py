#Descomponer un número
numero = int(input ("introdue el numero."))

umil = numero //1000
x = numero % 1000
centenas = x // 100
x = x % 100
decenas = x // 10
unidades = x % 10

print(umil,"M +",centenas,"C +",decenas,"D +",unidades,"U +")