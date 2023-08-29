#Conversión de Decimal a Binario
n = int(input("Ingrese numero: "))
pasarBin = bin(n)
lista = list(str(pasarBin))
lista.remove("0")
lista.remove("b")
print("resultado="+"".join(lista))