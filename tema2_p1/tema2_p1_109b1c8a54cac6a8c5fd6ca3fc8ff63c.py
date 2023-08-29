#Hito 1 primo
def es_primo(n):
    if n==1:
            return False
    a=range(2,n)
    for i in a:
        if (n%i)==0:
            return False
        else:
            return True
           