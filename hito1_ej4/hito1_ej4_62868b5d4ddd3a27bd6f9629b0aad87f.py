#Conversión de Decimal a Binario
n = int(input("ingrese el numero decimal:"))
t=n
conteo=0
while n>=1:
    n=n//2
    conteo+=1
print("resultado=",(bin(t)[2:conteo+2]))