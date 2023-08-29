
bin = ""

num = int(input('Ingresa un numero: '))

while num != 0: 
    
    modulo = num % 2
    cociente = num // 2
    bin = bin + str(modulo)
    num = cociente
binario = bin[::-1]
print("resultado=",binario)

