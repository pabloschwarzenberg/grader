#Descomponer un número
numero=input("Introduce el número: ")
numero=""
mil =int( numero / 1000)
tmp = int( numero % 1000)

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print("Unidades de millar: %i", umil)
print("Centenas: %i", centenas)
print("Decenas: %i", decenas)
print("Unidades: %i" , unidades)