#Conversión de Decimal a Binario
n = int(input("Ingrese número: "))

b = 0
i = 0
while n > 0:
    b = (n % 2)*10**i + b
    n //= 2
    i+=1

print("resultado="+str(b))
