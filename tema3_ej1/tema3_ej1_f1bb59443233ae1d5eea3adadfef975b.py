def suma_divisores(a):
    div = [1]
    if a != 1:
        for n in range(2, a):
            if a % n == 0:
                div.append(n)
    if a != 1:
        for n in range(2, a + 1):
            if a % n == 0:
                return sum(div), False
            else:
                return sum(div), True
    else:
        return 0, False

print(suma_divisores(13))