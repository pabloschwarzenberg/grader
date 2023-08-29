def es_primo(numero):
    i = 2
    divisor = 0
    if numero > 2:
        while i != numero:
            if numero % i == 0:
                divisor += 1
            i += 1
    if numero == 1:
        return False
    elif divisor == 0:
        return True
    else:
        return False