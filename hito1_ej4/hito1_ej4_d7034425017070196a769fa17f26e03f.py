#Conversión de Decimal a Binario
num = eval(input("ingrese el numero: "))
lista = []
while num>=1:
    lista.insert(0, num%2)
    num = num // 2
resultado = "".join(str(i) for i in lista)
print("resultado=", resultado)