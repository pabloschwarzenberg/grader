#Conversión de Decimal a Binario
decimal =int(input("ingrese un numero entero:" ))
lista = []
while decimal>=1:
  lista.insert(0,decimal%2)
  decimal=decimal//2
resultado = "".join(str(i) for i in lista)
print("resultado=",resultado)