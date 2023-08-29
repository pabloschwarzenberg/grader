def divisores(num):
    div = []
    sum = 0
    for i in range(1, num):
        if (num % i) == 0:
            div.append(i)
    for j in div:
        sum += j
    return sum

def amigos(a, b):
    c = divisores(a)
    d = divisores(b)
    if c == b and d == a:
        return True
    else:
        return False

