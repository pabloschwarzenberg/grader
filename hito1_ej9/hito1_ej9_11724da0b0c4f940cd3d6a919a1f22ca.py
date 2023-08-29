#Sistema de Ecuaciones
N1 = int(input("Ingrese el primer valor -> "))
N2 = int(input("Ingrese el segundo valor -> "))
N3 = int(input("Ingrese el tercer valor -> "))
N4 = int(input("Ingrese el cuarto valor -> "))
N5 = int(input("Ingrese el quinto valor -> "))
N6 = int(input("Ingrese el sexto valor -> "))


def S(N1,N2,N3,N4,N5,N6):
    D = N1 * N5 - N2 * N4
    if (D != 0):
        x = (N3 * N5 - N2 * N6)/D
        y = (N1*N6 - N3*N4)/D
        print("x=", x, "y=", y)
    else:
        return None, None

print(S(N1,N2,N3,N4,N5,N6))