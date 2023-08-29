#Descomponer un número
numero = float(input("Ingresa el número de 4 cifras: "))
print (" ")
umil = numero / 1000
tmp = numero % 1000
centenas = tmp / 100
tmp = tmp % 100
decenas = tmp / 10
unidades = tmp % 10
print ("Descomposición Horizontal")
print (" ")
print ("[","%i"%umil,"M +","%i" % centenas,"C +","%i" % decenas,"D +","%i" % unidades,"U","]")      