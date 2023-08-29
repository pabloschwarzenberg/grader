# por favor escribe aquí tu función
def es_primo(a):
    div=2
    b=0
    if a==1:
        b=False
    if div<a:
        while a%div!=0:
            div=div+1
        if a%div==0:
            b=False
    if div==a:
        b=True
    return b
    
           