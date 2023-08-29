def SumaDivisores(n):
 suma = 0

    for i in range(1, n + 1):
        if n % i == 0:
            suma += i

    return suma

print(sumaDivisores(n))
