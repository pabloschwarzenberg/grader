#Conversión de Decimal a Binario
NUM = int(input("ingrese un numero decimal"))
bin(NUM)
print("resultado=" + str(int(bin(NUM)[2:])))      