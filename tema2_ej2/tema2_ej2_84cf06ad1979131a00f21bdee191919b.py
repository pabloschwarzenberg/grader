def suma(N, S):
    for i in range(2, N):
        if (N % i == 0):
            S = S + i
    return S


sum1, sum2 = 1, 1
n1 = int(input("ingrese primer numero\n"))
n2 = int(input("ingrese segundo numero\n"))
sum1 = suma(n1, sum1)
sum2 = suma(n2, sum2)
if ((sum1 == n2) and (sum2 == n1)):
    print("TRUE")
else:
    print("FALSE")