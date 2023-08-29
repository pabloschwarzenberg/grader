def suma_divisores(a):
    ads = 0
    for ad in range(1, a):
        if a % ad == 0:
            ads += ad
    if (ads == 1):
        primo = True
    else:
        primo = False
    return ads, primo    