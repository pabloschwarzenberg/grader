n = int(input("n: "))

lista = []

binario = ""

while n >= 1:
    lista.insert(0,n%2)
    n = n // 2
resultado = binario.join(str(i) for i in lista)

print("resultado=",resultado)