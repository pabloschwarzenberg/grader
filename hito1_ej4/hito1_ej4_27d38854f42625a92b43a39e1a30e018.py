#Conversión de Decimal a Binario
numero=int(input("Escriba un numero decimal"))
n=str(bin(numero))
n=int(n[2::])
print("resultado=",n)