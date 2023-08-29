# por favor escribe aquí tu función
def es_primo(numero):
    a=2
    b=3
    i=0
    while numero>3 and i<=0:
        if numero%a==0 or numero%b==0:
            b=False
        else:
            b=True
        i=i+1
        
    if numero==1:
        b=False
    elif 1<numero<4:
        b=True
    return b