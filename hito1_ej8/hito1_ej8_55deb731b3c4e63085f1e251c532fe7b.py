#Descomponer un número
N = input("Ingrese su número: ")
if len(str(N)) == 4:
    U = str(N[3])
    D = str(N[2])
    C = str(N[1])
    M = str(N[0])
    print(M, "M +", C, "C +", D,"D +",U,"U")
elif len(str(N)) == 3:
    U = str(N[2])
    D = str(N[1])
    C = str(N[0])
    print(C, "C +", D,"D +",U,"U")
elif len(N) == 2:
    U = str(N[1])
    D = str(N[0])
    print(D,"D +",U,"U")
elif len(N) == 1:
    U = str(N[0])
    print(U,"U")
else:
    print("Error")