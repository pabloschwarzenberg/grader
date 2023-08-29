#Descomponer un número
numero = int(input("Ingrese un numero de hasta 4 cifras: "))

milesimas = numero//1000
centenas = (numero%1000)//100
decenas = (numero//10)%10
unidades = numero%10

mensaje = str(milesimas) + "m + " + str(centenas) + "c + " + str(decenas) + "d + " + str(unidades) + "u"

print(mensaje)      