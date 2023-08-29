#Conversión de Decimal a Binario
decimal = int(input("ingrese el decimal que desea convertir a binario: "))

bin(decimal)

print("resultado=",(int(bin(decimal)[2:])))