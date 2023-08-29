def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    else:
        divisor = 5
        while divisor * divisor <= numero:
            if numero % divisor == 0 or numero % (divisor + 2) == 0:
                return False
            divisor += 6
        return True
    
    