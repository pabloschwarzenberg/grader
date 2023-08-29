#Descomponer un número
numero = int(input("Ingrese un numero de  cuatro digitos: "))
#Calcular la Unidad
unidad = numero%10
#print(numero, x)
numero //= 10
#Calcular la Decena
decena = numero%10
#print(numero, y)
numero //= 10
#Calcular la Centena
centena = numero%10
#print(numero, z)
numero //= 10
#Calcular la Unidad de Mil
miles = numero%10
#print(numero, w)
numero //= 10

if miles != 0:
    print("{}M+{}C+{}D+{}U".format(miles,centena,decena,unidad))

elif centena != 0:
    print("{}C+{}D+{}U".format(centena, decena, unidad))

elif decena != 0:
    print("{}D+{}U".format(decena, unidad))

elif unidad != 0:
    print("{}U".format(unidad))

else:
    print("Error")