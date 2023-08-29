def amigos(a, b):
    divA = []
    divB = []
    a = int(a)
    b = int(b)
    for i in range(1, a+1):
        if a % i == 0:
            divA.append(i)
    for i in range(1, b+1):
        if b % i == 0:
            divB.append(i)

    sumA = sum(divA)
    sumB = sum(divB)

    if sumA == sumB and a != b:
        return True
    else:
        return False