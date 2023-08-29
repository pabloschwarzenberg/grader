#Ordenar tres números
N1 = int(input('Ingrese primer numero: '))
N2 = int(input('Ingrese segundo numero: '))
N3 = int(input('Ingrese tercer numero: '))

if (N1 <= N2) and (N1 <= N3) and (N2 <= N3):
    print(N1, ',', N2, ',', N3)
if (N1 <= N2) and (N1 <= N3) and (N3 <= N2):
    print(N1, ',', N3, ',', N2)

if (N2 <= N1) and (N2 <= N3) and (N1 <= N3):
    print(N2, ',', N1, ',', N3)

if (N2 <= N1) and (N2 <= N3) and (N3 <= N1):
    print(N2, ',', N3, ',', N1)

if (N3 <= N1) and (N3 <= N2) and (N1 <= N2):
    print(N3, ',', N1, ',', N2)

if (N3 <= N1) and (N3 <= N2) and (N2 <= N1):
    print(N3, ',', N2, ',', N1)