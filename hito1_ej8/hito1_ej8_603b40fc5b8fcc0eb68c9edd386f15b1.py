#Descomponer un número
N = int(input("Inserte un numero cualquiera: "))
N = str(N)
L = len(N)

if L == 4:
    print(N[0], "M +", N[1], "C +", N[2], "D +", N[3], "U")
elif L == 3:
    print(N[0], "C +", N[1], "D +", N[2], "U ")
elif L == 2:
    print(N[0], "D +", N[1], "U ")
elif L == 1:
    print(N[0], "U ")