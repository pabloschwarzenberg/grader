def es_primo(numero):
    for m in range(2, 10):
        if numero%m ==0:
            return False
        elif numero == 1:
            return False
        else:
            return True
print(es_primo(1))