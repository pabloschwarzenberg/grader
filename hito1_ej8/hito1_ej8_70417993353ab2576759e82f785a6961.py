#Descomponer un número
numero = int(input ("Introduce el número: "))

umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10


cadena = ""
UM = "%i" % umil

if (len(str(numero))>3):
    cadena = str(UM) + "M + "

CN = "%i" % centenas
if (len(str(numero))>2):
    cadena = cadena + str(CN) + "C + " 


DE = "%i" % decenas
if (len(str(numero)) > 1):
    cadena = cadena + str(DE) + "D +"


UN = "%i" % unidades
if (len(str(numero))>0):
    cadena = cadena + str(UN) + "U"


print (cadena)