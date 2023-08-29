numero = int(input("Coloque un numero mayor o igual de 4 cifras: "))

mil = numero / 1000
div = numero % 1000

centena = div / 100
div = div % 100

decena = div / 10
unidad = div % 10

print("M: %i" % mil)
print("C: %i" % centena)
print("D: %i" % decena)
print("U: %i" % unidad)

if mil<=0:
    print(centena, "C + ",decena, "D +", unidad, "U")
    if centena<=0:
        print(decena, "D +", unidad, "U")
        if decena<0:
            print(unidad, "U")
if mil>0:
 print("%i" % mil, "M +", "%i" % centena, "C +","%i" % decena, "D +", "%i" % unidad, "U ")