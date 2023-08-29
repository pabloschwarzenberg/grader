# completa el código de la función
def suma_divisores(a):
    sumdiv = 0
    i = 1
    while i < a:
        if a % i == 0:
            sumdiv = sumdiv + i
        i = i + 1

    if sumdiv == 1:
        return (sumdiv, True)
    else:
        for i in range(2, sumdiv//2+1):
            if sumdiv % i == 0:
                return (sumdiv, True)
        return (sumdiv, False) 