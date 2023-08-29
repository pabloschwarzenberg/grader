# completa el código de la función
def suma_divisores(a):
    count = 0
    for x in range(1, a):
        if a % x == 0:
            count = count + x
        
    if count == 1:
        return count, True
    else:
        return count, False