#Descomponer un número
N = float(input("Introduce el número que quiere descomponer -> "))

UM = N / 1000
x = N % 1000
C = x / 100
x = x % 100
D = x / 10
U = x % 10

print("M: %i" % UM)
print("C: %i" % C)
print("D: %i" % D)
print("U: %i" % U)

if (UM <= 0):
    print(C, "C + ",D, "D +", U, "U")
    if (C <= 0):
        print(D, "D +", U, "U")
        if (D < 0):
            print(U, "U")
if (UM > 0):
    print("%i" % UM, "M +", "%i" % C, "C +","%i" % D, "D +", "%i" % U, "U")    