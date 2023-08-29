def es_primo(num, n=2):
    if num == 0 or num == 1 or num == 4:
        return False
    for x in range(2, int(num/2)):
        if num % x == 0:
            return False
    return True