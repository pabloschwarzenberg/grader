#Descomponer un número
n = int(input("Ingrese un numero: "))
Unidades = n % 10
Decenas = n // 10 % 10
Centenas = n // 100 % 10
Milesimas = n // 1000 % 10
print(str(Milesimas) + "M+" + str(Centenas) + "C+" + str(Decenas) + "D+" + str(Unidades) + "U")    