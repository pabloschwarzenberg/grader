#Conversión de Decimal a Binario
n=float(input("Ingrese un número decimal: "))
binario=0
m=1
while n!=0:
    binario = binario + n % 2 * m
    n //= 2
    m *= 10
print(binario)