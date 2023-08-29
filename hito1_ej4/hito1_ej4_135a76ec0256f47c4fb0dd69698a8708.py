#Conversión de Decimal a Binario
n = int(input("Ingrese un numero: "))

n = n//1

n = bin(n)

n = n[2:1000]


print("Resultado=", n)