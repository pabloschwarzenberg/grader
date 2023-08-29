#Ordenar tres números
#Entradas
N_1 = int(input("Ingrese número 1: "))
N_2 = int(input("Ingrese número 2: "))
N_3 = int(input("Ingrese número 3: "))
#Procedimiento
if N_1 < N_2 and N_2 < N_3:
    print(N_1, ",", N_2, ",", N_3)

if N_2 < N_1 and N_1 < N_3:
    print(N_2, ",", N_1, ",", N_3)

if N_3< N_1 and N_1 < N_2:
    print(N_3,",", N_1,",", N_2)

if N_3 < N_2 and N_2 < N_1:
    print(N_3, ",", N_2, ",", N_1)

if N_1 < N_3 and N_3 < N_2:
    print(N_1, ",", N_3, ",", N_2)

if N_2 < N_3 and N_3 < N_2:
    print(N_2, ",", N_3,",", N_1)

#Procedimiento 2
if N_1 == N_2 and (N_3 > N_1 and N_2):
    print(N_1, ",", N_2, ",", N_3)
if N_1 == N_2 and (N_1 and N_2 > N_3):
    print(N_3, ",", N_1, ",", N_2)
if N_1 == N_3 and (N_2 > N_1 and N_3):
    print(N_1, ",", N_3, ",", N_2)
if N_1 == N_3 and (N_1 and N_3 > N_2):
    print(N_2, ",", N_1, ",", N_3)
if N_2 == N_3 and (N_1 > N_2 and N_3):
    print(N_1, ",", N_2, ",", N_3)
if N_2 == N_3 and (N_2 and N_3 > N_1):
    print(N_2, ",", N_3, ",", N_1)

      