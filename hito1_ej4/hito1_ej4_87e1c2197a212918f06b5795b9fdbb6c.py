#Conversión de Decimal a Binario
numero = int(input( " ingrese un numero decimal: " ))
lista= []
while numero >= 1 :
    lista.insert(0,numero%2)
    numero = numero // 2
binario = "" .join(str(i) for i in lista)
resultado = int (binario)
print ( "resultado = " ,resultado )
      