# por favor escribe aquí tu función
def es_primo(a):
    n=2
    if a==1:
        return False
    while n<a:
        r=a%n
        if r==0:
            return False
        else:
            n+=1
            continue
    if n==a:
        return True

           