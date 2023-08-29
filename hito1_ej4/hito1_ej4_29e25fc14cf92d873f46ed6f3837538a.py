#Conversión de Decimal a Binario
n = int(input("Ingrese un numero: "))
lista = []

while n > 0:
    x = n//2
    r = n%2        
    r = str(r)
    lista.append(r)
    n = x

lista = lista[::-1]
result = "".join(lista[0:])
print("resultado=", result)
