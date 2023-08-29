# por favor escribe aquí tu función
def divisores(n):
    divisor=1 
    cantidad_divisor=0
    while divisor<=n:
        if n%divisor==0:
            cantidad_divisor+=1
        divisor+=1
    return cantidad_divisor
def es_primo(n):
    if n%2==0:
        if n==2:
            return True
        else:
            return False
    elif n%2!=0:
        if divisores(n)!=2:
            if n==2:
                return True
            else:
                return False
        else:
            return True
        
