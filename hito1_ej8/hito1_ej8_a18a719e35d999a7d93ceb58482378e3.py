numero = int(input("Introduce el número: "))

umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print(" %iM" % umil, "+ %iC" % centenas,"+ %iD" % decenas,"+ %iU" % unidades)