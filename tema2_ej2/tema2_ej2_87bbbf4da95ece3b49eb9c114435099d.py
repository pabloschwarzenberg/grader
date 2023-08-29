def amigos(a, b):
    plusa = 0
    plusb = 0
    for i in range(1, a):
        if a % i == 0:
            plusa += i

    for x in range(1, b):
        if b % x == 0:
            plusb += x

    return plusa == b and plusb == a