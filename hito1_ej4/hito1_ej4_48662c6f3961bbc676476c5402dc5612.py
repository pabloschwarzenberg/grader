#Conversión de Decimal a Binario
n = int(input("Ingrese un número: "))

bin = ""
    
if n == 0:
    bin = "0"
else:    
    while n > 0:
        bin = str(n % 2) + bin
        n = n // 2

print("resultado={}".format(bin))