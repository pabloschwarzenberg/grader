#Descomponer un número
n = float(input("Introduce el número: "))
umil = n/ 1000
x = n % 1000
centenas = x / 100
x = x % 100
decenas = x / 10
unidades = x % 10
print("M: %i" % umil)
print("C: %i" % centenas)
print("D: %i" % decenas)
print("U: %i" % unidades)
if umil<=0:
    print(centenas, "C + ",decenas, "D +", unidades, "U")
    if centenas<=0:
        print(decenas, "D +", unidades, "U")
        if decenas<0:
            print(unidades, "U")
if umil>0:
    print("%i" % umil, "M +", "%i" % centenas, "C +","%i" % decenas, "D +", "%i" % unidades, "U")
     