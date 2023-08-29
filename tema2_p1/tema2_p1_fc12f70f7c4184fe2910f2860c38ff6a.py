# por favor escribe aquí tu función
def es_primo(n):
    c=0
    for f in range(1,n+1):
        if n%f==0:
            c= c+1
    if c==2:
        return True
    else:
        return False  