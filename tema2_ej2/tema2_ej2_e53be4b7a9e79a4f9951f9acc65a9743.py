def amigos(a,b):  
    def Divisores(x):
        Lista_divisores = []
        for i in range(1, x):
            if x % i == 0:
                Lista_divisores.append(i)
        Suma_Div = int(sum(Lista_divisores))
        return Suma_Div
    Divisores(a)
    Divisores(b)
    if Divisores(a) == b:
        return True
    return False
           