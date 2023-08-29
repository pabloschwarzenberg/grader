# por favor escribe aquí tu función
def es_primo(n):
        d=2
        while d<n:
            if n%d==0 or n==1:
                return False
                break
            d=d+1
        if n==1:
            return False
        return True