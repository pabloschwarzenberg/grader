#Conversión de Decimal a Binario
n=str(bin(int(input("Ingrese su número: "))))
#los binarios empiezan desde la derecha, el [2:] es para que evite imprimir "0b" al principio
print("resultado=",n[2:])