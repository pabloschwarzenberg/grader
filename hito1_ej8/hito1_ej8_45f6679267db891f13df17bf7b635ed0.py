#Descomponer un número
print("Introduce el número de hasta 4 digitos a descomponer: ")
x = int(input())

unidadmil = x / 1000
resultado = x % 1000

centenas = resultado / 100
resultado = resultado % 100

decena = resultado / 10
unidad = resultado % 10


print("%i" % unidadmil,"M +","%i" % centenas,"C +" +"%i" % decena,"D +","%i" % unidad,"U")     