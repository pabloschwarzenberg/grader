def es_primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for n in range(2, int(numero)):
        if numero % n == 0:
            return False
        else:
            return True
