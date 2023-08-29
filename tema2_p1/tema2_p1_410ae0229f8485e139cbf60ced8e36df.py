# por favor escribe aquí tu función
def es_primo(n):
    a=n-1
    if n==1:
        return False
    else:
        while a>1:
            if n%a==0:
                return False
            a-=1
        return True
    
         







    