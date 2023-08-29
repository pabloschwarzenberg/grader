# Factores Primos
n = int(input())
factores = []
a = n


def es_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if 0 == numero % i:
                return False
        return True


k = 1
t = n
j = 2
while k != n:
    if t % j == 0 and es_primo(j):
        factores.append(j)
        k = k * j
        t = t / j
    else:
        j = j + 1

for m in range(len(factores)):
    print(factores[m])
