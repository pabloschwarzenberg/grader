#Conversión de Decimal a Binario0
n=int(input("Ingrese un numero"))
a=int("%08d" % int(bin(n)[2:]))
print("resultado=",a)
      