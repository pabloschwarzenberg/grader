#Conversión de Decimal a Binario
num = int(input(""))
resto = ""
while num:
    resto = str(num % 2) + resto
    num //= 2
print("resultado=", resto)