def numero_perfecto(a):
    return False

def numero_perfecto(x):
    y=0
    for a in range(1, x):
        if x%a==0:
            y += a

    return y == x

           