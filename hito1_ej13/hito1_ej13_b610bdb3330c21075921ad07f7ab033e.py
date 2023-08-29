n = int(input())
separador = "\n"
primos = []
for i in range(2, n+1):
        while n % i == 0:
            primos.append(i)
            n = n // i
            if n == 1:
                print(primos)

