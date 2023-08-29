a = eval(input("Ingrese el numero: "))
lista = []
while (a >= 1):
 lista.insert(0, a%2)
 a = (a // 2)
resultado = "".join(str(i) for i in lista)
print("resultado=", resultado)