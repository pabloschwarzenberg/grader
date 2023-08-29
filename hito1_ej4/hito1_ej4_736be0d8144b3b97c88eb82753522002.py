#Conversión de Decimal a Binario
n = input("ingrese un numero :")
dec_number = int(n)
bin_number = bin(dec_number)
x = bin_number[2:]
print("resultado=",x)