#Descomponer un número
num=int(input("Ingrese un número: "))

#Unidades de mil
umil = num / 1000
resto = num % 1000

cent = resto / 100
resto = resto % 100

dec = resto / 10
unid = resto % 10

print("%iM"% umil,"+ %iC" % cent,"+ %iD" % dec, "+ %iU" % unid)
