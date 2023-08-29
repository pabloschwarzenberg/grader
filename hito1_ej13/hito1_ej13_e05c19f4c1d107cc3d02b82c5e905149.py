# Factores Primos
def es_primo(numero):
    if numero == 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


num = int(input())
num2 = num

for i in range(num, 0, -1):
    if es_primo(i):
        while num2 % i == 0:
            print(i)
            num2 //= i
