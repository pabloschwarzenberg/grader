# por favor escribe aquí tu función
def es_primo(numero):
    c=0
    if numero==1:
        c=10
    if numero==2:
        c=1
    else:
        for i in range(1,numero):
            if numero%i==0:
                c=c+1
            if numero%i==1:
                c=c
    if c>1:
        return False
    else :
        return True
           