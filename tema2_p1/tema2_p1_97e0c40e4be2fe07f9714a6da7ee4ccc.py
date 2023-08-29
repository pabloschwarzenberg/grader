#numeros primos
def es_primo(num):
    if num == 1:
        return False
    elif num == 2: 
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
for i in range(1, 101):
    print(i, es_primo(i))