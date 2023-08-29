#Conversión de Decimal a Binario
num = eval(input("Ingrese un numero: "))
binario = ""
binariof = ""
for i in range(num):
    if num % 2 == 0:
        binario += "0"
        num = num // 2
    else:
        binario += "1"
        num = num // 2
    
    if num == 1:
        binario += "1"
        break

longitudbin = len(binario)

for i in range(longitudbin):
    binariof += binario[longitudbin - i - 1]
    
print("resultado=" , str(binariof)) 