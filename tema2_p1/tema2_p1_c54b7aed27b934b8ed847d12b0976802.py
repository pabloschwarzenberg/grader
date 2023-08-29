# por favor escribe aquí tu función
def es_primo(n):
    r=2
    while r<n:
        if (n%r)==0:
            return False
        r=r+1
    if r==n:
        return True
    else:
        return False
     