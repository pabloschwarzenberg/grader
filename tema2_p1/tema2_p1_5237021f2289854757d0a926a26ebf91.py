def es_primo(a):
    ads = 0
    for da in range(1, a):
        if (a % da == 0):
            ads += da
    if (ads == 1):
        primo = True
    else:
        primo = False
    return primo