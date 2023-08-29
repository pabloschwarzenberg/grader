x = int(input())


def conver(k):
    primos = []

    for i in range(2, k + 1):
        while k % i == 0:
            primos.append(i)
            k = k / i
            
    for i in range(len(primos)):
        print(primos[i])

conver(x)