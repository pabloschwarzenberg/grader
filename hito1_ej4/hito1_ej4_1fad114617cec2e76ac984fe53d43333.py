n = int(input("ingresa un numero: "))
binario = ""

while n > 0:
   resto = n % 2
   binario = str(resto) + binario
   n = n//2

print(binario)
      