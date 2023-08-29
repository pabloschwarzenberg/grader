#Conversión de Decimal a Binario
n = eval(input("ingrese un número para pasarlo a binario: "))

#se escribe el método para convertir en binario
binario = bin(n)
#se imprime el resultado, insertando "00b" para evitar que se impriman digitos extras en la respuesta
print("resultado=",format(n, "00b"))



    