numero = float(input("Introduce el número: "))

miles = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print("M: %i" % miles)
print("C: %i" % centenas)
print("D: %i" % decenas)
print("U: %i" % unidades)

if miles<=0:
    print(centenas, "C + ",decenas, "D +", unidades, "U")
    if centenas<=0:
        print(decenas, "D +", unidades, "U")
        if decenas<0:
            print(unidades, "U")
if miles>0:
    print("%i" % miles, "M +", "%i" % centenas, "C +","%i" % decenas, "D +", "%i" % unidades, "U")