# por favor escribe aquí tu función
def es_primo(n):
    d=2
    primo=True
    while d<n:
        if n%d==0:
            primo=False
            break
        d=d+1
    if primo and n>1:
        return True
    else:
        return False
    


          