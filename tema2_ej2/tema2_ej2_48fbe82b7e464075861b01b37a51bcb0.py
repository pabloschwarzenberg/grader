# completa el código de la función
def amigos(a,b):
    lista2=0
    lista1=0
    for i in range(1,a):
        if a%i==0:
            lista1+=i
    for k in range(1,b):
        if b%k==0:
            lista2+=k

    if lista1==b and lista2==a:
        return True
    else:
        return False