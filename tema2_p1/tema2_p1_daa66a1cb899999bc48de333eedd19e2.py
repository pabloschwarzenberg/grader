def es_primo(numero):
    n=numero
    divisores=0
    while n !=0:
        if numero % n==0:
            divisores+=1
            n-=1
        else:
            n-=1
    if divisores == 2:
        return True
    else:
        return False
