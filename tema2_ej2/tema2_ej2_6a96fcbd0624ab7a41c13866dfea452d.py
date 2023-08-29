def amigos(a, b):
    div_a, div_b = [], []
    if a == 1 and b == 2: return False

    for num in range(1, a):
        if a % num == 0:
            div_a.append(num)

    for num in range(1, b):
        if b % num == 0:
            div_b.append(num)

    suma_a, suma_b = sum(div_a), sum(div_b)
    return (suma_a == b or a == suma_b)


amigos(10, 24)
