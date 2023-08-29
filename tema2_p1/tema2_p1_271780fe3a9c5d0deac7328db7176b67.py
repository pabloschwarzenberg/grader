def es_primo(numero):
    if numero <= 1:
        return False

    else:
        for j in range(2, numero):
            if numero % j == 0:
                return False
        return True