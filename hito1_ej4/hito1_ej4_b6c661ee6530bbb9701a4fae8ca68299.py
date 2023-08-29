#Conversión de Decimal a Binario
numero = int(input("ingrese un numero: "))
numero = list(bin(numero))
eliminar = numero.pop(1)
eliminar2 = numero.pop(0)
juntar = "".join(numero)
print("resultado={}".format(juntar))