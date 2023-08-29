#Descomponer un número
numero = int(input("Ingresa un número de hasta 4 dígitos: "))

unidades = numero % 10
decenas = (numero // 10) % 10
centenas = (numero // 100) % 10
miles = (numero // 1000) % 10

print(str(miles) + "M + " + str(centenas) + "C + " + str(decenas) + "D + " + str(unidades) + "U")
