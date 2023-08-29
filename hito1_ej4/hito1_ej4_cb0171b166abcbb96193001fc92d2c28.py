#Conversión de Decimal a Binario
#Conversión de Decimal a Binario
n = int(input("Ingresa un numero decimal para convertirlo a binario:"))

L =  list(bin(n))
L.pop(0)
L.remove("b")

n="".join(L)
print(str("resultado=")+str(n))
    