valor1 = int(input("Ingresar un número :"))
lista = []


while valor1 >= 1:
    lista.insert(0,valor1%2)
    valor1 = valor1 // 2
resultado = "".join(str(i) for i in lista)

print("resultado =", resultado)
     