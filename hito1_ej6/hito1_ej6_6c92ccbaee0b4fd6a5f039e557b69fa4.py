#Ordenar tres números
N1 = int(input("Ingrese numero: "))
N2 = int(input("Ingrese numero: "))
N3 = int(input("Ingrese numero: "))
if N1 < N2 < N3:
    print(N1,N2,N3)
elif N1 < N3 < N2:
    print(N1, N3, N2)
elif N2 < N3 < N1:
    print(N2, N3, N1)
elif N2 < N1 < N3:
    print(N2, N1, N3)
elif N3 < N1 < N2:
    print(N3, N1, N2)
else:
    print(N3, N2, N1)