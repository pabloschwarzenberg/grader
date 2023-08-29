#Conversión de Decimal a Binario
decimal=int(input("Ingrese un numero decimal: "))
lista = list(bin(decimal))
lista.pop(0)
lista.remove("b")
decimal = "".join(lista)

print("resultado=",decimal)