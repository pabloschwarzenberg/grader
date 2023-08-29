#Conversión de Decimal a Binario
numero= float(input("ingrese numero para hacerlo binario:"))
binario=" "
num= numero
while num//2!=0:
    binario= str(round(num%2))+binario
    num= num//2
final= str(round(num))+binario
print("resultado=", int(final))
