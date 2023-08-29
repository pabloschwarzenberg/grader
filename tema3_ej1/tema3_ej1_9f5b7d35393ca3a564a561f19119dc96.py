def es_primo(numero):
    if numero==1 or numero%2==0:
        n=False
    else:
        n=True
    return n

def suma_divisores(a):
    i=1
    acum=0
    while i<a:
        if a%i==0:
            acum=acum+i
        i=i+1
    
    return (acum,es_primo(a))



           