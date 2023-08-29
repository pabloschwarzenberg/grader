#Descomponer un número
N = int(input("Ingrese Número: "))

U = 0
D = 0
C = 0
M = 0

n = N

while N > 0:
    if N >= 1000:
        N = N - 1000
        M = M + 1
    elif N >= 100:
        N = N - 100
        C = C + 1
    elif N >= 10:
        N = N - 10
        D = D + 1
    elif N >= 1:
        N = N - 1
        U = U + 1

if M and C and D and U != 0:
    print(M,"M +", C,"C +", D,"D +", U, "U")
if C and D and U != 0 and (M == 0):
    print(C,"C +", D,"D +", U, "U")
if D and U != 0 and (M and C == 0):
    print(D,"D +", U, "U")
if U != 0 and (M and C and D == 0):
    print(U, "U")