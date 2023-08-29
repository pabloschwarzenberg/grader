def numero_perfecto(a):
    x = 0 
    for i in range(1,a):
        if a % i == 0:
            x = x + i
    if x == a:
        return True
    return False