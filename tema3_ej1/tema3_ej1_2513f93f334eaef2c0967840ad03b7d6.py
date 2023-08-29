# completa el código de la función
def suma_divisores(a):
    n = int(a)
    total = 0
    primo = False
    for i in range(n-1):
        if n%(i+1) == 0:
            total += (i+1)

    if total == 1:
        primo = True
        
    return total, primo