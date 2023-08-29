           def es_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

print(es_primo(2))  # True
print(es_primo(7))  # True
print(es_primo(10)) # False
print(es_primo(15)) # False
print(es_primo(23)) # True
