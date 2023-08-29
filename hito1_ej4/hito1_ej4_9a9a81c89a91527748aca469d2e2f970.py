#Conversión de Decimal a Binario

num_decimal = int(input("ingrese su numero:"))
bin(num_decimal)
a = int(bin(num_decimal)[2:])
print("resultado=",a)