def suma_divisores(n):
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
    if sum(div) == 1:
        return sum(div), True
    if sum(div) > 1:
        return sum(div), False
    if sum(div) == 0:
        return sum(div), False