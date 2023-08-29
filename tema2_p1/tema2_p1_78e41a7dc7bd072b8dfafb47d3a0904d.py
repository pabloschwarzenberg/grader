def es_primo(numero, n=2):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    # para sacar los multiplos
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True 

