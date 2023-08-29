x = int(input("Ingrese el número que desea convertir: "))

lista = list(bin(x))

lista.pop(0)

lista.remove("b")


x = "".join(lista)

print("resultado=",x)