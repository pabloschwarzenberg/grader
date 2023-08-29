#Conversion de decimal a binario
n = eval(input("ingrese un numero: "))
bin(n)
binario = int(bin(n)[2:])
print("el resultado =",binario)