#Conversión de Decimal a Binario
n=int(input("ingresa un numero decimal: "))
print("resultado=" + str(int(bin(n)[2:])))  