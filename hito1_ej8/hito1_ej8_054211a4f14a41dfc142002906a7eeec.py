print ("Introduce el número: ")
numero = int(input ())

umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = numero % 100

decenas = tmp / 10
tmp = numero % 10

unidades = tmp / 1
tmp = numero % 10
print ("%iM+" % umil, end = "")
print ("%iC+" % centenas, end = "")
print ("%iD+" % decenas, end = "")
print ("%iU" % unidades, end = "")