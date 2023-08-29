#Descomponer un número
N= float(input("Introduce el número: "))
S = N / 1000
tmp = N % 1000

C = tmp / 100
tmp = tmp % 100

D = tmp / 10
U = tmp % 10

print("M: %i" % S)
print("C: %i" % C)
print("D: %i" % D)
print("U: %i" % U)

if S<=0:
    print(C, "C + ",D, "D +", U, "U")
    if C<=0:
        print(D, "D +", U, "U")
        if D<0:
            print(U, "U")
if S>0:
    print("%i" % S, "M +", "%i" % C, "C +","%i" % D, "D +", "%i" % U, "U")      