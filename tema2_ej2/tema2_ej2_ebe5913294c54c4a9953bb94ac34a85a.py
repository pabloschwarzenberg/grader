def amigos(a, b):
    divs_a, divs_b = 0, 0
    for divisor in range(1, a):
        if a % divisor == 0:
            divs_a += divisor
    for divisor in range(1, b):
        if b % divisor == 0:
            divs_b += divisor
    if divs_a == b and divs_b == a:
        return True
    else:
        return False  