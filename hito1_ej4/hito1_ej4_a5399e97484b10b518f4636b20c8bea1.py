#Conversión de Decimal a Binario
numero = eval(input("Ingrese el numero: "))
lista = []
while numero>=1:
    lista.insert(0, numero%2)
    numero = numero // 2
resultado = "".join(str(i) for i in lista)
print("resultado=", resultado)      