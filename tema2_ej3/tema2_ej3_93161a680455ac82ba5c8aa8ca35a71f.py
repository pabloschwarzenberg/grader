def numero_perfecto(a):
    c = 1
    sum = 0
    while c < a:
        if a % c == 0:
            sum += c
        c += 1
    if sum == a:
        return True
    else:
        return False