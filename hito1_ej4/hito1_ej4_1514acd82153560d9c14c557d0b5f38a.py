n = int(input("Ingrese un número: "))
lista = []

while n >= 1:
    lista.insert(0, n%2)
    n = n // 2
resultado = "".join(str(i) for i in lista)

print("resultado=" + str(resultado))