#Numeros primos
def es_primo(n):
    if n==1:
     return False
    G=True
    a=2
    b=3
    c=5
    d=7
    F1=True
    r=True
    l=True
    m=True
    o=True
    if n==a:
     r=False
    if n==b:
        l=False
    if n==c:
        m=False
    if n==d: 
        o=False
    while G and F1: 
     if n%a==0 and r:
        G=False
        return False
    
     elif n%b==0 and l:
        G=False
        return False
     elif n%c==0 and m:
        G=False
        return False
     elif n%d==0 and o:
        G=False
        return False
     else:
        G=True
        F1=False
        return True

    




           