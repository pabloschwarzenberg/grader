def numero_perfecto(n):
    b = 1
    a = 0
    while b != n:
        if n % b == 0:
            a = a + b
        b = b + 1
    if a == n:
        return True
    else:
        return False