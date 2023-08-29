# Benjamín Kock
numero1=int(input("ingrese un número: "))
numero2=int(input("ingrese otro número: "))
def suma(N, S):
    for i in range(2, N):
        if (N % i == 0):
            S = S + i
    return S
sum1, sum2 = 1, 1
sum1 = suma(numero1, sum1)
sum2 = suma(numero2, sum2)
if ((sum1 == numero2) and (sum2 == numero1)):
    return True
else:
    return False