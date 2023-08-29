#descomponer un numero de hasta 4 digitos
print("Introduce el número de hasta 4 digitos a descomponer: ")
x = int(input())

umil = x / 1000
resultado = x % 1000

centenas = resultado / 100
resultado = resultado % 100

decenas = resultado / 10
unidades = resultado % 10


print("%i" % umil,"M +","%i" % centenas,"C +" +"%i" % decenas,"D +","%i" % unidades,"U")

