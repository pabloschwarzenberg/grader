#Conversión de Decimal a Binario
#Entrada
n = int(input("Ingrese un numero decimal: "))
binario = ''

while n > 0:
    binario = str(n % 2) + binario
    n //= 2

#Salida
print ("Resultado=" + binario)