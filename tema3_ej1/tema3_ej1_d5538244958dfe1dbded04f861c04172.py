def suma_divisores(a):
    n = 1
    div = 0
    while n < a:
        if a % n == 0:
            div += n
        n += 1
    if div > 1 and a != 1:
        new_div = (div, False)
    elif a == 1:
        new_div = (div, False)
    else:
        new_div = (div, True)
    return new_div