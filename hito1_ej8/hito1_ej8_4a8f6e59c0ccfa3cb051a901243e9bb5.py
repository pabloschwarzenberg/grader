#Descomponer un número
numero = eval(input("ingresa un numero de 4 cifras: "))

unidadesmil = (numero//1000) % 10
centenas = (numero//100) % 10
decenas = (numero//10) % 10
unidades = (numero//1) % 10

print(unidadesmil,"M + ",centenas,"c + ",decenas,"D + ",unidades,"U")