# por favor escribe aquí tu función
def es_primo(n):
    d=2
    if n>1:
        while n%d!=0 and d!=n:
            n%d
            d=d+1
        if d==n:
            return True
        elif d!=n:
            return False
    if n<=1:
        return False
           