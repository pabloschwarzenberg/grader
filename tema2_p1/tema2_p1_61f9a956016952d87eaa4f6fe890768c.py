# por favor escribe aquí tu función
def es_primo(numero):
    i=1
    b=0
    while i<=numero:
        if numero%i!=0:
            i+=1
        elif numero%i==0:
            i+=1
            b+=1
    else:
        if b==2:
            c=True
        elif b!=2:
            c=False
        return c
           