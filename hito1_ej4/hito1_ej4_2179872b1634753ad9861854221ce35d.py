#Conversión de Decimal a Binario

n = int(input("Ingrese un número: "))
n = bin(n)
n = n[2:len(n)]

print("Resultado=", n)