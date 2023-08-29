def numero_perfecto(a):
    total = 0
    for numero in range(1, a - 1):
        if (a%numero == 0):
            total += numero
    if a == total:
        return True 
    else:
        return False
           