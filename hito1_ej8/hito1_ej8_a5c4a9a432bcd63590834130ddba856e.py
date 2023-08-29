#Descomponer un número
numero = float(input("Introducir un numero de 4 digitos: "))
unmil = numero / 1000
tmp = numero % 1000
centenas = tmp / 100
tmp = tmp % 100
decenas = tmp / 10
unidades = tmp % 10
print("M: %i" % unmil)
print("C: %i" % centenas)
print("D: %i" % decenas)
print("U: %i" % unidades)
if unmil<=0:
    print(centenas, "C + ",decenas, "D +", unidades, "U")
    if centenas<=0:
        print(decenas, "D +", unidades, "U")
    if decenas<0:
        print(unidades, "U")
if unmil>0:
    print("%i" % unmil, "M +", "%i" % centenas, "C +","%i" % decenas, "D +",
"%i" % unidades, "U")   