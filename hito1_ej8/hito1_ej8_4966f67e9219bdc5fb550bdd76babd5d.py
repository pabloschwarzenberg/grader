#Descomponer un número
numero = int(input("Ingrese un numero de 4 digitos: "))

miles = numero // 1000
centenas = (numero % 1000) // 100
decenas = (numero % 100) // 10
unidades = (numero % 10) // 1

print(miles ,"M", "+", centenas,"C", "+", decenas,"D", "+", unidades ,"U")