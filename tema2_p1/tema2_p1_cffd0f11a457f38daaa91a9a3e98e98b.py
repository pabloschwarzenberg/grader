def es_primo(numero):
    if numero!=1:
        for n in range(2, numero):
            if numero % n == 0:
                return False
        return True
    else:
        return False